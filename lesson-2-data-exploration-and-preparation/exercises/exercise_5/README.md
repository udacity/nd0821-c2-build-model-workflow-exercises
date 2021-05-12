# Instructions
In this exercise you will create a MLflow component that preprocess the data. 
It implements in a reusable way the steps we implemented in the EDA notebook in the previous exercise (exercise 4).

## Steps

Write the ``conda.yml`` file, the ``MLproject`` file and fill in the ``run.py`` script.

Remember, your script must execute the following operations:
1. Download the input artifact (use ``exercise_4/genres_mod.parquet:latest``) from W&B
2. Open it with pandas (using ``pd.read_parquet``)
3. Drop duplicates (``df.drop_duplicates().reset_index(drop=True)`)
4. Add a new feature:
   ```python
   df['title'].fillna(value='', inplace=True)
   df['song_name'].fillna(value='', inplace=True)
   df['text_feature'] = df['title'] + ' ' + df['song_name']
   ```
   NOTE: again, in a real setting, you will have to make sure that your feature
   store provides this text_feature at inference time, OR, you will have to move
   the computation of this feature to the inference pipeline.
   
5. Save the result to a file and upload it to an artifact with name ``preprocessed_data.csv``

Hints:
1. Remember to set the experiment name when calling ``wandb.init``. Use ``exercise_5`` as project
   name.
2. Remember to use the artifact system from W&B to fetch the data (``use_artifact``)
   
3. You will need the following dependencies:
   ```yaml
   - pandas=1.2.3
   - pip=20.3.3
   - pyarrow=2.0
   - pip:
       - wandb==0.10.21
   ```
3. You do NOT need to generate the profiles from pandas-profiling (and you also do not need
   pandas-profiling as a dependency in ``conda.yml``)
4. Save the cleaned data in a new artifact on W&B called ``preprocessed_data.csv``
5. We are going to use the created artifact several times in the following exercises. Verify that
   you have an artifact called ``preprocessed_data.csv`` under the project ``exercise_5``, so the
   following command works:
   ```bash
   wandb artifact get exercise_5/preprocessed_data.csv
   ```
   If it doesn't, check your exercise and fix it. Do not move on unless the command executes
   successfully, otherwise you won't be able to do some of the next exercises.
   