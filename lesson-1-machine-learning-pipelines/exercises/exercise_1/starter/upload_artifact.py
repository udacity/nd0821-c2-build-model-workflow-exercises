#!/usr/bin/env python
import argparse
import logging
import pathlib
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    logger.info("Creating run exercise_1")

    # Create a W&B run in the project `exercise_1`. Set the option `job_type="upload_file"`:
    run = wandb.init(project="exercise_1", job_type="upload_file")
    # Create an instance of the class `wandb.Artifact`. Use the `artifact_name` parameter to
    # fill the keyword `name` when constructing the `wandb.Artifact` class. Use the parameters
    # `artifact_type` and `artifact_description` to fill respectively the keyword `type` and
    # `description`.
    # HINT: you can use args.artifact_name to reference the parameter artifact_name
    logger.info("Creating artifact")
    artifact = wandb.Artifact(
        name=args.artifact_name,
        type=args.artifact_type,
        description=args.artifact_description,
    )

    # Attach the file provided as the parameter `input_file` to the artifact instance using
    # `artifact.add_file`, and log the artifact to the run using `run.log_artifact`.
    artifact.add_file(args.input_file)

    logger.info("Logging artifact")
    run.log_artifact(artifact)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Upload an artifact to W&B", fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--input_file", type=pathlib.Path, help="Path to the input file", required=True
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
