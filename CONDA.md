# Conda Requirement for Exercises

## Why Conda is Required

The exercises in this repository use **MLflow** to orchestrate ML pipelines. MLflow relies on **conda** to create isolated, reproducible environments for each pipeline step.

Each exercise contains a `conda.yml` file that specifies the dependencies for that component. When you run:

```bash
mlflow run .
```

MLflow reads the `conda.yml` file and automatically creates a conda environment with the specified packages before executing the code.

## Installing Conda

If you don't have conda installed, you can install it via:

- **Miniconda** (recommended, lightweight): https://docs.conda.io/en/latest/miniconda.html
- **Anaconda** (full distribution): https://www.anaconda.com/download

## Virtual Environment (requirements.txt)

The `requirements.txt` file in the root directory contains all dependencies with pinned versions for the entire repository. This is useful for:

- Exploring the codebase
- Running standalone Python scripts
- IDE/editor support and autocompletion

To use it:

```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

However, **for running the actual exercises**, you still need conda installed because MLflow will create its own conda environments from the individual `conda.yml` files.

## Exercise Workflow

1. Install conda (Miniconda or Anaconda)
2. Navigate to an exercise directory (e.g., `lesson-1-machine-learning-pipelines/exercises/exercise_3/starter/`)
3. Run the pipeline: `mlflow run .`
4. MLflow will automatically create the conda environment and execute the code
