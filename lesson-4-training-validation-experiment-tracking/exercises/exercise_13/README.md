# Instructions
In this exercise you will build a component that fetches a model and test it on the test dataset.

Then, you will mark that model as "production ready".

In order to complete this exercise, go to the ``run.py`` file and complete the code when
requested by comments such as ``## YOUR CODE HERE``. Further instructions are provided there.

Then, run the component using the model exported in ``exercise_12`` 
(``exercise_12/model_export:latest``) and the test data (``exercise_6/data_test.csv:latest``).

Verify that the AUC and the confusion matrix look good, then go to the Artifact section in W&B
and add the tag ``prod`` to the model export artifact (``exercise_12/model_export:latest``) 
to mark is as "production-ready".
> HINT: to apply a new tag, go to the Artifact section of ``exercise_12``, click on 
> ``model_export`` and then select the ``latest`` version. Then go to the Aliases section, click
> on the `+` sign and add the tag ``prod``.