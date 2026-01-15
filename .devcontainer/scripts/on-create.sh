#!/bin/bash
set -e

echo "🚀 Setting up ML Workflow Exercises Codespace..."

# Activate conda environment
source /opt/conda/etc/profile.d/conda.sh
conda activate ml_workflow_base

# Create working directories
mkdir -p data mlruns outputs

echo "✓ Base environment ready: Python $(python --version)"
