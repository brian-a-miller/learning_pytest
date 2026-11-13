import pytest


@pytest.mark.slow
def test_long_running_process():
    # slow test that should not be run by default
    # maybe something that does a lot of computations
    # or makes slow network calls
    for i in range(0, 999999999):
        x = i / 2