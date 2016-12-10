"""Test for next_sq.py"""

import pytest
import math
from next_sq import find_next_square


SQRT_PARAMS_TABLE = [
    [121, 144],
    [625, 676],
    [319225, 320356],
    [15241383936, 15241630849],
    [155, -1],
    [342786627, -1]
]


@pytest.mark.parametrize('n, result', SQRT_PARAMS_TABLE)
def test_nextsq(n, result):
    """Run the basic test cases for find_next_square()"""
    assert find_next_square(n) == result


def solution(sq):
    """Provide solution for testing random numbers, from Code Wars"""
    root = sq ** 0.5
    return (root + 1) ** 2 if root % 1 == 0 else -1


def rest_randomsq():
    """Test random use cases for find_next_square() using solution()"""
    from random import randint, uniform
    for _ in range(40):
        sq = int(uniform(0, 1) * 10 ** randint(1, 5))
        if randint(0, 1): sq = sq * sq
        assert find_next_square(sq) == solution(sq)


"""Below are Code Wars' tests, which I've refactored.

Test.describe("find_next_square")

Test.it("should return the next square for perfect squares")
Test.assert_equals(find_next_square(121), 144, "Wrong output for 121")
Test.assert_equals(find_next_square(625), 676, "Wrong output for 625")
Test.assert_equals(find_next_square(319225), 320356, "Wrong output for 319225")
Test.assert_equals(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")

Test.it("should return -1 for numbers which aren't perfect squares")
Test.assert_equals(find_next_square(155), -1, "Wrong output for 155")
Test.assert_equals(find_next_square(342786627), -1, "Wrong output for 342786627")

Test.it("should work for random inputs")
from random import randint, uniform

def solution(sq):
    root = sq ** 0.5
    
    return (root + 1)**2 if root % 1 == 0 else -1

for _ in xrange(40):
    sq = int(uniform(0, 1) * 10 ** randint(1, 5))
    
    if randint(0, 1): sq = sq*sq
    
    message = "Wrong output for {sq}".format(sq=sq)
    Test.assert_equals(find_next_square(sq), solution(sq), message)
"""