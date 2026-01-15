# GitHub Codespaces Quick Start Guide

Welcome to the ML Workflow Exercises Codespace! This guide will help you get started in 5 minutes.

## First Time Setup

### 1. Create Your Codespace

Click the "Code" button in GitHub, select "Codespaces", then "Create codespace on master". Your Codespace will start building (takes ~2 minutes first time, ~30 seconds with prebuild).

### 2. Add Your Weights & Biases API Key

**Important**: All exercises require W&B authentication.

1. Get your API key from [https://wandb.ai/authorize](https://wandb.ai/authorize)
2. In GitHub, go to **Settings** → **Codespaces** → **Secrets**
3. Click **New secret**:
   - **Name**: `WANDB_API_KEY`
   - **Value**: [paste your API key]
   - **Repository access**: Select this repository
4. **Rebuild your Codespace**: Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows), type "Rebuild Container", and press Enter

### 3. Verify Setup

After rebuild, check the terminal output. You should see:
```
✓ WANDB_API_KEY found
✓ W&B login successful!
```

---

## Working with Exercises

### Lesson Structure

This repository contains 5 lessons with 16 exercises:
- **Lesson 1**: Machine Learning Pipelines (exercises 1-3)
- **Lesson 2**: Data Exploration and Preparation (exercises 4-6)
- **Lesson 3**: Data Validation (exercises 7-9)
- **Lesson 4**: Training, Validation, Experiment Tracking (exercises 10-13)
- **Lesson 5**: Final Pipeline, Release, and Deploy (exercises 14-16)

Each exercise has:
- `starter/` - Your workspace (with TODOs)
- `solution/` - Reference implementation

### Exercise Workflow

#### Navigate to Exercise
```bash
cd lesson-X-<lesson-name>/exercises/exercise_Y/solution
# Example:
cd lesson-3-data-validation/exercises/exercise_9/solution
```

#### Create Exercise Environment (First Time Only)
```bash
conda env create -f conda.yml
```

This creates a new conda environment with all dependencies. Takes ~1-2 minutes with mamba.

#### Activate Environment
```bash
conda activate <env_name>
```

The environment name is specified in `conda.yml`. Example names:
- `ex3_multi_step_env` (Lesson 1, Exercise 3)
- `ex7_env` (Lesson 3, Exercise 7)
- `ex14_env` (Lesson 5, Exercise 14)

#### Run Exercise

**MLflow projects** (most exercises):
```bash
mlflow run .
```

**pytest tests** (Lesson 3):
```bash
pytest . -v
```

**Jupyter notebooks** (Lesson 2):
```bash
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser
```
Then click the Jupyter Lab link that appears.

---

## Lesson-Specific Instructions

### Lesson 1: Machine Learning Pipelines
Basic MLflow pipeline construction. Learn to chain components.

**Key exercises**:
- Exercise 2: Single component pipeline
- Exercise 3: Multi-step pipeline (download → process)

**Common commands**:
```bash
cd lesson-1-machine-learning-pipelines/exercises/exercise_3/solution
conda env create -f conda.yml
conda activate ex3_multi_step_env
mlflow run .
```

### Lesson 2: Data Exploration and Preparation
EDA with pandas-profiling, data preprocessing.

**Key exercises**:
- Exercise 4: EDA with ydata-profiling
- Exercise 5: Data preprocessing pipeline

**Jupyter workflow**:
```bash
cd lesson-2-data-exploration-and-preparation/exercises/exercise_5/solution
conda env create -f conda.yml
conda activate ex5_env
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser
```

### Lesson 3: Data Validation
pytest-based data validation, statistical tests.

**Key exercises**:
- Exercise 7: Basic pytest tests
- Exercise 9: Kolmogorov-Smirnov test

**pytest workflow**:
```bash
cd lesson-3-data-validation/exercises/exercise_9/solution
conda env create -f conda.yml
conda activate ex9_env
pytest . -v --reference_artifact="..." --sample_artifact="..." --ks_alpha=0.05
```

### Lesson 4: Training & Experiment Tracking
Model training, hyperparameter tuning, W&B tracking.

**Key exercises**:
- Exercise 10: Random forest training
- Exercise 12: Experiment tracking

**Hyperparameter sweep**:
```bash
cd lesson-4-training-validation-experiment-tracking/exercises/exercise_10/solution
conda env create -f conda.yml
conda activate ex10_env
mlflow run . -P hydra_options="random_forest.n_estimators=100,200 random_forest.max_depth=10,50 -m"
```

### Lesson 5: Full Pipeline
Complete end-to-end ML pipeline with all components.

**Pipeline steps**: download → preprocess → check_data → segregate → train → evaluate

**Run specific steps**:
```bash
cd lesson-5-final-pipeline-release-and-deploy/exercises/exercise_14/solution
conda env create -f conda.yml
conda activate ex14_env

# Run specific steps
mlflow run . -P hydra_options="main.execute_steps='download,preprocess'"

# Run all steps
mlflow run .
```

---

## Common Issues

### "WANDB_API_KEY not set"
**Problem**: W&B authentication failed
**Solution**:
1. Check if you added the secret to GitHub Codespaces (Settings → Codespaces → Secrets)
2. Make sure the secret name is exactly `WANDB_API_KEY`
3. Rebuild your container (`Cmd+Shift+P` → "Rebuild Container")

### "conda: command not found"
**Problem**: Conda not activated
**Solution**: The base environment should activate automatically. If not:
```bash
source /opt/conda/etc/profile.d/conda.sh
conda activate ml_workflow_base
```

### "Disk space full"
**Problem**: Too many conda environments
**Solution**: Run the cleanup script:
```bash
bash .devcontainer/scripts/cleanup-mlflow-envs.sh
```
Or use the VS Code task: `Cmd+Shift+P` → "Tasks: Run Task" → "Cleanup MLflow Environments"

### "Environment <env_name> not found"
**Problem**: Haven't created the exercise environment yet
**Solution**: Run `conda env create -f conda.yml` in the exercise directory

### "Port 8888 already in use"
**Problem**: Jupyter Lab already running
**Solution**: Kill the existing process:
```bash
pkill -f jupyter
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser
```

### Slow execution / timeouts
**Problem**: Codespace resource constraints
**Solution**:
- Close unused browser tabs
- Stop unnecessary processes
- Consider upgrading to 8-core machine (Settings → Codespaces → Machine type)

---

## VS Code Tasks

Access via `Cmd+Shift+P` → "Tasks: Run Task":

- **Cleanup MLflow Environments**: Free up disk space
- **Create Exercise Environment**: Run `conda env create -f conda.yml`
- **Run MLflow Project**: Run `mlflow run .` (default task)
- **Run pytest**: Run pytest with verbose output
- **Start Jupyter Lab**: Launch Jupyter on port 8888

---

## Viewing Results

### MLflow UI
When you run `mlflow run .`, the MLflow UI becomes available:
1. Check the "Ports" tab in VS Code (bottom panel)
2. Click on the "MLflow UI" link (port 5000)
3. View experiments, parameters, metrics, and artifacts

### Weights & Biases
1. Go to [https://wandb.ai](https://wandb.ai)
2. Navigate to your project (e.g., `exercise_14`)
3. View runs, artifacts, and visualizations

---

## Free Tier Limits

GitHub Codespaces free tier includes:
- **60 core-hours per month** (for 4-core machine = 15 hours)
- **15 GB storage**
- **120 GB bandwidth**

**Tips to conserve**:
- **Stop Codespace when done**: Settings (⚙️) → Stop Codespace
- **Auto-stop timeout**: Set to 30 minutes (Settings → Codespaces → Timeout)
- **Delete unused Codespaces**: GitHub → Codespaces → Delete old ones
- **Use smaller machine type** for simple exercises (2-core is often sufficient)

---

## Tips & Best Practices

### Environment Management
- Each exercise gets its own conda environment
- Environment names are in `conda.yml` (check `name:` field)
- List all environments: `conda info --envs`
- Remove specific environment: `conda remove --name <env_name> --all`

### Working with Starter Files
The `starter/` directories contain TODO markers for you to implement:
- Follow exercise README.md for instructions
- Compare with `solution/` when stuck
- Both starter and solution use the same `conda.yml`

### Jupyter Notebooks
**Important**: Properly shut down Jupyter:
1. Save your work
2. File → Shut Down
3. Close browser tab
4. Kill terminal process (Ctrl+C)

**Never** just close the browser tab - this leaves Jupyter running and consuming resources.

### Port Forwarding
VS Code automatically forwards these ports:
- **5000**: MLflow UI (access via Ports tab)
- **8888**: Jupyter Lab (auto-opens in browser)
- **8889**: Jupyter Notebook (silent, for manual access)

---

## Getting Help

### Documentation
- **This file**: Quick start for Codespaces
- **README.md**: Full repository documentation
- **CLAUDE.md**: Architecture and patterns
- **Exercise README.md**: Specific instructions per exercise

### Common Commands Reference
```bash
# Navigate
cd lesson-X-*/exercises/exercise_Y/solution

# Environment
conda env create -f conda.yml
conda activate <env_name>
conda info --envs
conda remove --name <env_name> --all

# Run exercises
mlflow run .
mlflow run . -P steps=download
mlflow run . -P hydra_options="param=value"
pytest . -v
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser

# W&B
wandb login
wandb whoami
wandb status

# Cleanup
bash .devcontainer/scripts/cleanup-mlflow-envs.sh
```

---

## Next Steps

1. **Complete Lesson 1**: Learn MLflow basics
2. **Experiment with Lesson 2**: Try EDA with pandas-profiling
3. **Master Lesson 3**: Understand data validation
4. **Optimize in Lesson 4**: Run hyperparameter sweeps
5. **Build Lesson 5**: Create your full ML pipeline

Happy learning! 🚀
