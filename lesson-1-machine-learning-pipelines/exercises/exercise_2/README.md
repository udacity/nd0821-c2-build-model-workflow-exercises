# Instructions
In this exercise we will build our first MLflow component.

The starter kit contains a script called ``download_data.py`` that downloads a file and logs it
into W&B. The scope of this exercise is to transform this script into a MLFlow component.

The script can be run on its own as:

```bash
python download_data.py \
       --file_url https://raw.githubusercontent.com/scikit-learn/scikit-learn/4dfdfb4e1bb3719628753a4ece995a1b2fa5312a/sklearn/datasets/data/iris.csv \
       --artifact_name iris \
       --artifact_type raw_data \
       --artifact_description "The sklearn IRIS dataset"
```

## Steps
1. Create a ``conda.yml`` file declaring the dependencies of the script. The script needs
   the ``requests`` library at version ``2.24.0`` (``requests=2.24.0``) installed with conda, 
   as well as the W&B client ``wandb`` at version ``0.10.21`` *installed with pip* (you can use
   pip at version ``20.3.3``)
   
2. Create the ``MLproject`` file declaring the ``download_data.py`` script as ``main``, and fill
   up all the relevant sections, so the script can be run through mlflow. Remember to declare the
   parameters of the script, which are ``file_url``, ``artifact_name``, ``artifact_type``, and
   ``artifact_description``. For ``artifact_type``, provide a default of ``raw_data``. Use the 
   reference command reported at the beginning as a guide to fill up the ``command`` part.
   
3. Run the script with MLflow setting up the parameters as follow:
   * ``file_url=https://raw.githubusercontent.com/scikit-learn/scikit-learn/4dfdfb4e1bb3719628753a4ece995a1b2fa5312a/sklearn/datasets/data/iris.csv``
   * ``artifact_name=iris``
   * ``artifact_description="This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length"``
   
4. Check in your W&B account that the ``exercise_2`` project has been created, and that there is at
   least one version of the ``iris`` dataset.