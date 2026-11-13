import pytest
from example_math_functions import is_prime


def test_is_prime_negative():
    num = -4
    is_prime_result = is_prime(num)
    assert is_prime_result == False


def test_is_prime_2():
    assert is_prime(2)


# example of using parameterized tests
# dictionary specifies key-value pairs
# key: input value
# value: expected result
is_prime_parameterized_test_cases = {
    -1: False,
    0: False,
    1: False,
    2: True,
    3: True,
    4: False,
    5: True,
    6: False,
    7: True,
    17: True,
    18: False,
    97: True,
    100: False,
}

@pytest.mark.parametrize("num, expected", is_prime_parameterized_test_cases.items())
def test_is_prime_parameterized_tests(num, expected):
    assert is_prime(num) == expected
