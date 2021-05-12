import hydra
import mlflow
import os


# This automatically reads in the configuration
@hydra.main(config_name='config')
def go(config):

    os.environ["WANDB_PROJECT"] = config["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = config["main"]["experiment_name"]

    mlflow.run(...)


if __name__ == "__main__":
    go()
