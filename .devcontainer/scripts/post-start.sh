#!/bin/bash
set -e

echo ""
echo "=========================================="
echo "  ML Workflow Exercises - Codespace"
echo "=========================================="
echo ""

source /opt/conda/etc/profile.d/conda.sh
conda activate ml_workflow_base

echo "Environment: Python $(python --version 2>&1 | cut -d' ' -f2), MLflow $(mlflow --version 2>&1 | awk '{print $NF}')"
echo "Disk Space: $(df -h /workspaces | tail -1 | awk '{print $4}') available"
echo ""
echo "Quick Start:"
echo "  cd lesson-X-*/exercises/exercise_Y/solution"
echo "  conda env create -f conda.yml"
echo "  conda activate <env_name>"
echo "  mlflow run ."
echo ""
echo "Docs: README.md | CODESPACES_QUICKSTART.md"
