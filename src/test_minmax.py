"""Test for minmax.py"""

import pytest


MIN_PARAMS_TABLE = [
    [[-52, 56, 30, 29, -54, 0, -110], -110],
    [[42, 54, 65, 87, 0], 0],
    [[1, 2, 3, 4, 5, 10], 1],
    [[-1, -2, -3, -4, -5, -10], -10],
    [[9], 9],
    [[], []]
]

MAX_PARAMS_TABLE = [
    [[-52, 56, 30, 29, -54, 0, -110], 56],
    [[4, 6, 2, 1, 9, 63, -134, 566], 566],
    [[5], 5],
    [[534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555], 555],
    [[9], 9],
    [[], []]
]


@pytest.mark.parametrize('n, result', MIN_PARAMS_TABLE)
def test_mini(n, result):
    """Test the mini function"""
    from minmax import mini
    assert mini(n) == result


@pytest.mark.parametrize('o, result', MAX_PARAMS_TABLE)
def test_maxi(o, result):
    """Test the maxi function"""
    from minmax import maxi
    assert maxi(o) == result


def test_random_mini():
    """Test mini function using random numbers"""
    from random import randint
    from minmax import mini
    for _ in range(40):
        test_list = [(-1) ** randint(0, 1) * randint(1, 10 ** randint(1, 9)) for q in range(randint(1, 40))]
        assert mini(test_list) == min(test_list)


def test_random_max():
    """Test maxi function using random numbers"""
    from random import randint
    from minmax import maxi
    for _ in range(40):
        test_list = [(-1) ** randint(0, 1) * randint(1, 10 ** randint(1, 9)) for q in range(randint(1, 40))]
        assert maxi(test_list) == max(test_list)


"""
These were the original Code Wars tests.
Again, I had to refactor them due to their use of the Test class.

Test.describe("Basic tests")
Test.it("Fixed Min")
Test.assert_equals(min([-52, 56, 30, 29, -54, 0, -110]), -110)
Test.assert_equals(min([42, 54, 65, 87, 0]), 0)
Test.assert_equals(min([1, 2, 3, 4, 5, 10]), 1)
Test.assert_equals(min([-1, -2, -3, -4, -5, -10]), -10)
Test.assert_equals(min([9]), 9)

Test.it("Fixed Max")
Test.assert_equals(max([-52, 56, 30, 29, -54, 0, -110]), 56)
Test.assert_equals(max([4,6,2,1,9,63,-134,566]), 566)
Test.assert_equals(max([5]), 5)
Test.assert_equals(max([534,43,2,1,3,4,5,5,443,443,555,555]), 555)
Test.assert_equals(max([9]), 9)

Test.describe("Random Tests")
from random import randint

for _ in range(40):
    arr=[(-1)**randint(0,1)*randint(1,10**randint(1,9)) for q in range(randint(1,40))]
    Test.it("Testing for max in %s" %arr)
    Test.assert_equals(max(arr[:]),old_max(arr),"It should work for random inputs too")
    Test.it("Testing for min in %s" %arr)
    Test.assert_equals(min(arr[:]),old_min(arr),"It should work for random inputs too")
"""
