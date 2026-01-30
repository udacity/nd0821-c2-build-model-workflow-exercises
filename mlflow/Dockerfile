FROM ghcr.io/mlflow/mlflow:v3.8.1

# Note: This Dockerfile uses MLflow 3.8.1 base image, which may differ from
# the MLflow version (3.2.0) specified in conda.yml files throughout the repository.
# The newer version is used here to ensure compatibility with the latest features
# and security updates in the containerized MLflow server.

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    git \
 && rm -rf /var/lib/apt/lists/*

# Install Miniconda with architecture detection and checksum verification
ENV CONDA_DIR=/opt/conda
RUN set -e; \
    ARCH=$(uname -m); \
    if [ "$ARCH" = "x86_64" ]; then \
        MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-py311_24.11.1-0-Linux-x86_64.sh"; \
        MINICONDA_SHA256="7e0fb7c70c88d3da6ac50defe1ffeb5d0ca67d11f71b7ece321baa8ace6e65e4"; \
    elif [ "$ARCH" = "aarch64" ]; then \
        MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-py311_24.11.1-0-Linux-aarch64.sh"; \
        MINICONDA_SHA256="db89a0edc3a3a4ecd5a6e82f0d4f98dbd5d70560af183c0cd26299b0a5f34f82"; \
    else \
        echo "Unsupported architecture: $ARCH" >&2; \
        exit 1; \
    fi; \
    wget -q "$MINICONDA_URL" -O /tmp/miniconda.sh; \
    echo "$MINICONDA_SHA256  /tmp/miniconda.sh" | sha256sum -c -; \
    bash /tmp/miniconda.sh -b -p /opt/conda; \
    rm /tmp/miniconda.sh

# Update PATH to include conda
ENV PATH=$CONDA_DIR/bin:$PATH

# Make conda non-interactive
RUN conda config --set always_yes yes --set changeps1 no

# Accept Anaconda channel ToS (so `conda env create` won't fail)
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main \
 && conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# Force all processes/users (including mlflow projects) to use a global condarc
RUN mkdir -p /etc/conda \
 && printf "%s\n" \
  "channels:" \
  "  - https://repo.anaconda.com/pkgs/main" \
  "  - https://repo.anaconda.com/pkgs/r" \
  "channel_priority: strict" \
  > /etc/conda/.condarc

ENV CONDARC=/etc/conda/.condarc

# Clean up (optional but good)
RUN conda clean -afy

# Install additional dependencies if needed
COPY requirements.txt /tmp/pip-tmp/

RUN pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
 && rm -rf /tmp/pip-tmp


