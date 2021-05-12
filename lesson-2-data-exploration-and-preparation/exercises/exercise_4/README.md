# Instructions
In this exercise you will perform a simple Exploratory Data Analysis in Jupyter keeping track
of your progress with W&B.

Even though this step is interactive, and not based on scripts, we are still going to use MLflow
to ensure a reproducible analysis, by fixing the environment in the ``conda.yml`` file.

The starter kit contains already the environment definition (``conda.yml``).

> **_NOTE:_**  The dataset used in this exercise is a modified version of the original
> songs dataset: [here](https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify)

## Preliminary step
For this analysis we will use the provided ``genres_mod.parquet`` file. As a first step,
you need to upload the file to your W&B to track it:

```bash
wandb artifact put \
      --name exercise_4/genres_mod.parquet \
      --type raw_data \
      --description "A modified version of the songs dataset" genres_mod.parquet
```

## Steps

1. Create a ``MLproject`` file containing the ``main`` step. In this case, the step has no 
   parameters (you can skip completely the ``parameters`` section when defining ``main``) and
   the command is simply ``jupyter notebook``, which opens Jupyter.

2. Run the step (``mlflow run .``)
   
3. Create a notebook and call it ``EDA``
   
4. Within the notebook, import the relevant libraries (seaborn, pandas, wandb, pandas profiling), 
   then create a W&B run.
   NOTE: Remember to add the ``save_source=True`` option to ``wandb.init``
   
5. Fetch the artifact ``exercise_4/genres_mod.parquet:latest`` using W&B and read it with pandas
   HINT: 
   ```python
   artifact = run.use_artifact("exercise_4/genres_mod.parquet:latest")
   df = pd.read_parquet(artifact.file())
   df.head()
   ```
   
6. Generate a profile and note the warnings:
   ```python
   from pandas_profiling import ProfileReport
   
   profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
   profile.to_widgets()
   ```

7. Remove the duplicates:
   ```python
   df = df.drop_duplicates().reset_index(drop=True)
   ```
8. Let's perform a minimal feature enginnering. Let's create a new feature by concatenating
   them, after replacing all missing values with the empty string:
   ```python
   df['title'].fillna(value='', inplace=True)
   df['song_name'].fillna(value='', inplace=True)
   df['text_feature'] = df['title'] + ' ' + df['song_name']
   ```
   NOTE: this feature will have to go to the feature store. If you do not have a feature
   store, then you should not compute it here as part of the preprocessing step. Instead,
   you should compute it within the inference pipeline.

8. Optional: do some plotting with seaborn to get a better idea for the dataset:
   
7. When you are done, call ``run.finish()``, close the notebook and stop the jupyter 
   server by clicking on Quit in the main Jupyter page (upper right).
   **NOTE**: DO NOT use Crtl+C to shutdown Jupyter. That would also kill the mlflow job. 

8. Go to W&B, navigate to the run you just completed. You will see an option `{}` in the left
   panel. Click on it to see the uploaded Jupyter notebook.
   
