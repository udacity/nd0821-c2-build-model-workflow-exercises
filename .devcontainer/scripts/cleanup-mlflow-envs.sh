#!/bin/bash
set -e

echo "🧹 Cleanup MLflow conda environments..."

ENVS=$(conda info --envs | grep mlflow | cut -f1 -d" ")

if [ -z "$ENVS" ]; then
    echo "No MLflow environments to clean"
    exit 0
fi

echo "Found: $ENVS"
read -p "Remove all? (y/N) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    for env in $ENVS; do
        echo "Removing $env..."
        conda remove --name $env --all -y
    done
    echo "✓ Cleanup complete!"
else
    echo "Cancelled"
fi
