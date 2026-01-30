# Multi-stage build for efficiency
FROM condaforge/mambaforge:24.3.0-0 AS conda-builder

COPY environment.yml /tmp/environment.yml

# Create base environment with mamba (faster than conda)
RUN mamba env create -f /tmp/environment.yml --yes && \
    mamba clean -afy

# Final stage - Debian Bookworm base
FROM mcr.microsoft.com/devcontainers/base:bookworm

# Install system dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        build-essential \
        libopenblas-dev \
        liblapack-dev \
        git-lfs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy conda from builder
COPY --from=conda-builder /opt/conda /opt/conda

# Configure conda
ENV PATH="/opt/conda/bin:$PATH"
RUN /opt/conda/bin/conda init bash && \
    /opt/conda/bin/conda init zsh

WORKDIR /workspace
CMD ["/bin/bash"]
