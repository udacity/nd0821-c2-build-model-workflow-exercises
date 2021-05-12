# Instructions
In this exercise you will apply non-deterministic tests to the cleaned dataset from exercise 5.

For most of the non-deterministic tests you need a reference dataset, and a dataset to be tested.
This is useful when retraining, to make sure that the new training dataset has a similar
distribution to the original dataset and therefore the method that was used originally is expected
to work well.

Since we do not have a new training dataset, we will compare the test dataset against the train
dataset. This is a useful trick when obtaining a new training dataset right away is not possible.
The thresholds can be adjusted using K-fold cross validation.

Now go to the ``test_data.py`` script in the starter kit, and complete it by adding the
2-sample Kolmogorov-Smirnov test where indicated in the file. This is an example on how to apply it:

```python
import scipy.stats
import pandas as pd

# Read two dataframes
data1 = pd.read_csv(...)
data2 = pd.read_csv(...)

# Apply KS test to column "loudness"
col = "loudness"
scipy.stats.ks_2samp(data1[col], data2[col], alternative='two-sided')
```

Remember that the 2 sample KS test is used to test whether two vectors come from the same
distribution (null hypothesis), or from two different distributions (alternative hypothesis),
and it is non-parametric.