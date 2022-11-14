import pytest


@pytest.mark.usefixtures("data_sets")
def test_multiple_data(data_sets):
    print(data_sets)
