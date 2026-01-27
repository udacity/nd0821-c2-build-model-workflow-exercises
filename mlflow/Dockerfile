FROM ghcr.io/mlflow/mlflow:v3.8.1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    git \
 && rm -rf /var/lib/apt/lists/*

# Install Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O /tmp/miniconda.sh \
 && bash /tmp/miniconda.sh -b -p /opt/conda \
 && rm /tmp/miniconda.sh

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


