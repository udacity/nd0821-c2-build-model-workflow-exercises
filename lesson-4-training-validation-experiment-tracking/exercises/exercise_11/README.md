# Instructions
In this exercise we will perform experiments using a slightly improved version of the pipeline we 
developed in exercise 10, using the Hydra configuration management system.

The pipeline you find in the starter kit has been modified to allow to specify hyperparameters
related to the entire pipeline from the configuration file. Make sure to open ``config.yaml``
and familiarize yourself with its structure, in particular the new ``random_forest_pipeline``
section.

## Experiment 1
Let's start by overriding the ``max_depth`` parameter of the ``random_forest_pipeline.random_forest`` 
section of the configuration file (``config.yaml``):

```bash
mlflow run . -P hydra_options="random_forest_pipeline.random_forest.max_depth=5"
```

## Experiment 2
Now run another experiment overriding ``n_estimators`` in the ``random_forest`` section and setting 
it to 10.

## Experiment 3: sweep on ``max_depth``
Let's now exploit the sweep capability of Hydra to try several options for the ``max_depth``
parameter.

Let's start with a simple list and try the values 1, 5 and 10

> **NOTE**: remember to add the ``-m`` option at the beginning, otherwise the sweep will not
> work.

Now let's do something more advanced, and use the ``range`` operator of Hydra. Remember that
``range(1,10,2)`` means all the integers between 1 and 50 in increments of 2. Use the
``range`` operator to try ``max_depth`` from 1 to 10 in increments of 2 (5 jobs).

> **NOTE**: do not put any space within the range specification. So ``range(1,10,2)`` works, but
> ``range(1, 10, 2)`` does not!

## Experiment 4: sweep on multiple parameters
Now let's do a proper sweep and optimize multiple parameters. We can use a range operator on 
``random_forest_pipeline.random_forest.max_depth`` (let's do ``range(10,50,3)``) and one on 
``random_forest_pipeline.tfidf.max_features`` (let's do ``range(50,200,50)``).

Since this corresponds to several jobs, let's use the parallel feature so the jobs will run
in parallel on your machine. Just add ``hydra/launcher=joblib`` to the ``hydra_options``.

> **NOTE**: in order to use the joblib launcher you have to install hydra-joblib-launcher. Indeed, it is
> in our conda.yml file (among the pip dependencies)

Despite this being around 80 jobs, it should only take a few minutes to complete (depending on 
the speed of your computer and your internet, between 5 and 10 minutes).

## Select best performing model
Now you can go to W&B and select the best performing model.

The easiest way to do so is to select "Columns" in the upper right, deselect all columns and then
add only ``random_forest.max_depth``, ``tfidf.max_features`` and AUC. Then click on the three 
dots of the AUC column and select "Sort desc" to sort in descending order. The job at the top 
will be the job with the best performances.
