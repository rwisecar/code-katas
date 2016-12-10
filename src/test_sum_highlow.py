"""Test for sum_highlow.py"""

import pytest

SUM_HIGH_LOW_PARAMS_TABLE = [
    [None, 0],
    [[], 0],
    [[3], 0],
    [[-3], 0],
    [[3, 5], 0],
    [[3, -5], 0],
    [[6, 2, 1, 8, 10], 16],
    [[6, 0, 1, 10, 10], 17],
    [[-6, -20, -1, -10, -12], -28],
    [[-6, 20, -1, 10, -12], 3],
]


@pytest.mark.parametrize("n, result", SUM_HIGH_LOW_PARAMS_TABLE)
def test_basic_high_low(n, result):
    """Test the basic cases for the sum_array function"""
    from sum_highlow import sum_array
    assert sum_array(n) == result


def test_random_high_low():
    """Test sum_array with random inputs, taken from Code Wars"""
    from random import randint
    from functools import reduce
    from sum_highlow import sum_array
    sol = lambda arr: 0 if not arr or len(arr) < 3 else reduce(lambda a, b: a-b, reduce(lambda a, b: [a[0]+b, b if a[1] > b else a[1], b if a[2] < b else a[2]], arr, [0, 9999999999999, -9999999999999]))
    for _ in range(40):
        arr = [(-1) ** randint(0, 1) * randint(1, 10** randint(1, 3)) for q in range(randint(1, 45))]
        assert sum_array(arr) == sol(arr)


""" Here are the Code Wars test cases that I have refactored:
Test.describe("Basic tests")
Test.it("None or Empty")
Test.assert_equals(sum_array(None), 0)
Test.assert_equals(sum_array([]), 0)

Test.it("Only one Element")
Test.assert_equals(sum_array([3]), 0)
Test.assert_equals(sum_array([-3]), 0)

Test.it("Only two Element")
Test.assert_equals(sum_array([ 3, 5]), 0)
Test.assert_equals(sum_array([-3, -5]), 0)

Test.it("Real Tests")
Test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
Test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
Test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
Test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)

Test.describe("Random tests")
from random import randint
from functools import reduce; sol=lambda arr: 0 if not arr or len(arr)<3 else reduce(lambda a,b: a-b, reduce(lambda a,b: [a[0]+b, b if a[1]>b else a[1], b if a[2]<b else a[2]], arr, [0,9999999999999,-9999999999999]))

for _ in range(40):
  arr=[(-1)**randint(0,1)*randint(1,10**randint(1,3)) for q in range(randint(1,45))]
  Test.it("Testing for "+repr(arr))
  Test.assert_equals(sum_array(arr[:]),sol(arr),"It should work for random inputs too")
"""