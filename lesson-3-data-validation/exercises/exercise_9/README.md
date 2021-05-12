# Instructions
In this exercise we will modify the non-deterministic test we prepared in the previous exercise,
by allowing it to accept the reference dataset, the new dataset as well as the threshold
for the statistical test from the command line. This is fundamental for configurability and
reusability.

# Steps
1. Edit the ``conftest.py`` file, modifying the special ``pytest_addoption`` function so that
   pytest will accept the ``--ks_alpha`` option from the command line. Then modify the 
   ``ks_alpha`` fixture to process that parameters.
   
2. Modify ``test_data.py`` so that the test ``test_kolmogorov_smirnov`` will accept the data
   as well as the threshold as parameters
   
3. Run the test using mlflow and the artifacts ``exercise_6/data_train.csv:latest`` and 
   ``exercise_6/data_test.csv:latest`` respectively as reference and as sample artifacts, and use
   a reasonable threshold for the KS test (like 0.05). The tests will pass
   
4. Try again using a much higher threshold for the KS test (like 0.9). The test will fail.
   Can you say why?
