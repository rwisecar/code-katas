"""Test monkey.py module"""

import pytest
from monkey import monkey_count

""" Below are the test cases provided by Code Wars, which I refactored:
Test.describe("Basic tests")
Test.assert_equals(monkey_count(5), [1, 2, 3, 4, 5])
Test.assert_equals(monkey_count(3), [1, 2, 3])
Test.assert_equals(monkey_count(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
Test.assert_equals(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Test.assert_equals(monkey_count(20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

Test.describe("Random tests")
from random import randint
sol_count=lambda n: range(1,n+1)

for _ in xrange(40):
    n=randint(1,100)
    Test.it("Testing for %s" %n)
    Test.assert_equals(monkey_count(n),sol_count(n),"It should work for random inputs too")
"""

MONKEY_PARAMS_TABLE = [
    [5, [1, 2, 3, 4, 5]],
    [3, [1, 2, 3]],
    [9, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    [20, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
]


@pytest.mark.parametrize('n, result', MONKEY_PARAMS_TABLE)
def test_basic_monkey(n, result):
    """Test the basic use cases for monkey_count.py"""
    assert monkey_count(n) == result


def test_random_monkey():
    """Test random use cases for monkey_count.py
    Taken from Code Wars."""
    from random import randint
    sol_count = lambda n: list(range(1, n+1))
    for _ in range(40):
        n = randint(1, 100)
        assert monkey_count(n) == sol_count(n)
