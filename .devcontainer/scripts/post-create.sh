#!/bin/bash
set -e

echo "🔧 Running post-create setup..."

source /opt/conda/etc/profile.d/conda.sh
conda activate ml_workflow_base

# Verify installations
python --version
mlflow --version
wandb --version

# Handle W&B authentication
if [ -z "$WANDB_API_KEY" ]; then
    echo ""
    echo "⚠️  WARNING: WANDB_API_KEY is not set!"
    echo ""
    echo "To complete setup:"
    echo "  1. Go to https://wandb.ai/authorize"
    echo "  2. Copy your API key"
    echo "  3. GitHub Settings → Codespaces → Secrets → New secret"
    echo "     Name: WANDB_API_KEY"
    echo "     Value: [your key]"
    echo "  4. Rebuild container (Cmd+Shift+P → 'Rebuild Container')"
    echo ""
else
    echo "✓ WANDB_API_KEY found"
    wandb login --relogin <<< "$WANDB_API_KEY"
    echo "✓ W&B login successful!"
fi
