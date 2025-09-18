import pandas as pd
import wandb
import tempfile
import os

# Initialize W&B with the exercise_5 project
run = wandb.init(project="exercise_5", job_type="preprocess_data")

# Download the input artifact from W&B
artifact = run.use_artifact("exercise_4/genres_mod.parquet:latest")
artifact_dir = artifact.download()

# Read the parquet file from the downloaded artifact
df = pd.read_parquet(os.path.join(artifact_dir, "genres_mod.parquet"))

# Drop duplicates and reset index
df = df.drop_duplicates().reset_index(drop=True)

# Add new text feature
df['title'].fillna(value='', inplace=True)
df['song_name'].fillna(value='', inplace=True)
df['text_feature'] = df['title'] + ' ' + df['song_name']

# Save to CSV
df.to_csv("preprocessed_data.csv", index=False)

# Create and upload the new artifact
artifact = wandb.Artifact(
    name="preprocessed_data.csv",
    type="dataset",
    description="Preprocessed dataset with duplicates removed and text feature added"
)
artifact.add_file("preprocessed_data.csv")
run.log_artifact(artifact)

# Finish the run
run.finish()

