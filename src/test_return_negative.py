"""This is the test file for return_negative.py."""

import pytest
from random import randint as rnd
from return_negative import make_negative

PARAMS_TABLE = [
    [42, -42],
    [-9, -9],
    [0, 0]
]


@pytest.mark.parametrize('n, result', PARAMS_TABLE)
def test_return_negative(n, result):
    assert make_negative(n) == result


def test_random_positive_negative():
    number = rnd(1, 1000)
    assert make_negative(number) == -abs(number)


def test_random_negative_negative():
    number = rnd(-1000, 0)
    assert make_negative(number) == -abs(number)


# Code Wars' Tests:
# Test.assert_equals(return_negative(42),-42)
# Test.assert_equals(return_negative(-9),-9)
# Test.assert_equals(return_negative(0),0)

# from random import randint as rnd

# for _ in range(10):
#     number = rnd(1, 1000)
#     Test.assert_equals(return_negative(number),-abs(number))
#     number = rnd(-1000,0)
#     Test.assert_equals(return_negative(number),-abs(number))
