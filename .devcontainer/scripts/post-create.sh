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
    echo "  2. Copy your NEW v1 API key (format: wandb_v1_...)"
    echo "  3. GitHub Settings → Codespaces → Secrets → New secret"
    echo "     Name: WANDB_API_KEY"
    echo "     Value: [your key]"
    echo "  4. Rebuild container (Cmd+Shift+P → 'Rebuild Container')"
    echo ""
    echo "📝 NOTE: v1 API keys are longer (86 chars) and more secure."
    echo ""
else
    echo "✓ WANDB_API_KEY found"
    # Verify key format
    if [[ $WANDB_API_KEY == wandb_v1_* ]]; then
        echo "✓ Using v1 API key format (secure)"
    else
        echo "⚠️  Legacy API key detected. Consider upgrading to v1 format."
    fi
    wandb login --relogin <<< "$WANDB_API_KEY"
    echo "✓ W&B login successful!"
fi

# Configure persistent conda auto-activation (runs AFTER Oh My Zsh setup)
echo ""
echo "🔧 Configuring shell auto-activation..."

# Configure for zsh (default terminal)
if [ -f ~/.zshrc ]; then
    # Check if already configured (avoid duplicates on rebuilds)
    if ! grep -q "conda activate ml_workflow_base" ~/.zshrc; then
        echo "" >> ~/.zshrc
        echo "# Auto-activate ml_workflow_base conda environment" >> ~/.zshrc
        echo "conda activate ml_workflow_base 2>/dev/null || true" >> ~/.zshrc
        echo "✓ Zsh auto-activation configured"
    else
        echo "✓ Zsh auto-activation already configured"
    fi
fi

# Configure for bash (fallback)
if [ -f ~/.bashrc ]; then
    if ! grep -q "conda activate ml_workflow_base" ~/.bashrc; then
        echo "" >> ~/.bashrc
        echo "# Auto-activate ml_workflow_base conda environment" >> ~/.bashrc
        echo "conda activate ml_workflow_base 2>/dev/null || true" >> ~/.bashrc
        echo "✓ Bash auto-activation configured"
    else
        echo "✓ Bash auto-activation already configured"
    fi
fi

echo "✓ Shell configuration complete!"
