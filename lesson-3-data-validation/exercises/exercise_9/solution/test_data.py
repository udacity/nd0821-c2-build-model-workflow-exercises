import scipy.stats
import pandas as pd
import numpy as np

def _clean_series(s: pd.Series) -> pd.Series:
    # Convert to numeric (coerce bad strings), drop NaN/inf
    s = pd.to_numeric(s, errors="coerce")
    s = s.replace([np.inf, -np.inf], np.nan).dropna()
    return s


def test_kolmogorov_smirnov(data, ks_alpha):

    sample1, sample2 = data

    columns = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "duration_ms"
    ]

    alpha_prime = 1 - (1 - ks_alpha)**(1 / len(columns))

    for col in columns:

        s1 = _clean_series(sample1[col])
        s2 = _clean_series(sample2[col])

        # Guard against empty after cleaning (skip or fail with message)
        assert len(s1) > 0 and len(s2) > 0, f"Empty series after cleaning for column: {col}"

        ts, p_value = scipy.stats.ks_2samp(s1, s2)

        # Fail if p_value is NaN (shouldn't happen after cleaning)
        assert not np.isnan(p_value), f"NaN p-value for column: {col}"

        # NOTE: as always, the p-value should be interpreted as the probability of
        # obtaining a test statistic (TS) equal or more extreme that the one we got
        # by chance, when the null hypothesis is true. If this probability is not
        # large enough, this dataset should be looked at carefully, hence we fail
        assert p_value > alpha_prime, f"KS test failed for {col}: p={p_value:.4g} ≤ {alpha_prime:.4g}"
