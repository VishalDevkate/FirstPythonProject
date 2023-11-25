import pytest


def add_two_numbers(a, b):
    return a + b


@pytest.mark.math
@pytest.mark.positive
def test_small_numbers():
    assert add_two_numbers(3, 7) == 10, "3 + 7 should be 10"


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(430, 340) == 132, "430 + 340 equals 770"
