#!/usr/bin/env python
import argparse
import logging
import seaborn as sns
import pandas as pd
import wandb

from sklearn.manifold import TSNE

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="process_data")

    logger.info("Downloading artifact")
    artifact = run.use_artifact(args.input_artifact)
    artifact_path = artifact.file()

    iris = pd.read_csv(
        artifact_path,
        skiprows=1,
        names=("sepal_length", "sepal_width", "petal_length", "petal_width", "target"),
    )

    target_names = "setosa,versicolor,virginica".split(",")
    iris["target"] = [target_names[k] for k in iris["target"]]

    logger.info("Performing t-SNE")
    tsne = TSNE(n_components=2, init="pca", random_state=0)
    transf = tsne.fit_transform(iris.iloc[:, :4])

    iris["tsne_1"] = transf[:, 0]
    iris["tsne_2"] = transf[:, 1]

    g = sns.displot(iris, x="tsne_1", y="tsne_2", hue="target", kind="kde")

    logger.info("Uploading image to W&B")
    run.log({"t-SNE": wandb.Image(g.fig)})

    logger.info("Creating artifact")

    iris.to_csv("clean_data.csv")

    artifact = wandb.Artifact(
        name=args.artifact_name,
        type=args.artifact_type,
        description=args.artifact_description,
    )
    artifact.add_file("clean_data.csv")

    logger.info("Logging artifact")
    run.log_artifact(artifact)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a file and upload it as an artifact to W&B",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True,
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_type", type=str, help="Type for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_description",
        type=str,
        help="Description for the artifact",
        required=True,
    )

    args = parser.parse_args()

    go(args)
