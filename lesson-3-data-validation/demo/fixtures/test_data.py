import pytest
import wandb
import pandas as pd

run = wandb.init()

@pytest.fixture(scope="session")
def data():

    local_path = run.use_artifact("exercise_5/preprocessed_data.csv:latest").file()
    df = pd.read_csv(local_path, low_memory=False)

    return df


def test_data_length(data):
    """
    We test that we have enough data to continue
    """
    assert len(data) > 1000


def test_number_of_columns(data):
    """
    We test that we have enough data to continue
    """
    assert data.shape[1] == 19

# This is what pytest does:
# var = data()
# test_data_length(data=var)

# scope=session
# var = data()
# test_data_length(data=var)
# test_other_test_using_data(data=var)

# scope=function
# var = data()
# test_data_length(data=var)
# var = data()
# test_other_test_using_data(data=var)