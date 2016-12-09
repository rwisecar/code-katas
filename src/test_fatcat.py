"""Test for fatcat.py"""

import pytest
from fatcat import bonus_time

FATCAT_PARAMS_TABLE = [
    [10000, True, '$100000'],
    [25000, True, '$250000'],
    [10000, False, '$10000'],
    [60000, False, '$60000'],
    [2, True, '$20'],
    [78, False, '$78'],
    [67890, True, '$678900'],
]


@pytest.mark.parametrize("m, n, result", FATCAT_PARAMS_TABLE)
def test_bonus(m, n, result):
    """Test the basic use cases for bonus_time()"""
    assert bonus_time(m, n) == result


def test_random_bonus():
    """Test random use cases, using Code Wars' tests."""
    from random import randint
    sol = lambda s, b: "$%s" % (s * (10 if b else 1))
    for _ in range(40):
        s = randint(1, 10 ** randint(2, 4)) * 100
        b = [False, True][randint(0, 1)]
        assert bonus_time(s, b) == sol(s, b)

"""Below are Code Wars tests, which I have refactored.
Test.describe("Basic tests")
Test.assert_equals(bonus_time(10000, True), '$100000')
Test.assert_equals(bonus_time(25000, True), '$250000')
Test.assert_equals(bonus_time(10000, False), '$10000')
Test.assert_equals(bonus_time(60000, False), '$60000')
Test.assert_equals(bonus_time(2, True), '$20')
Test.assert_equals(bonus_time(78, False), '$78')
Test.assert_equals(bonus_time(67890, True), '$678900')

Test.describe("Random tests")
from random import randint
sol=lambda s, b: "$%s" %(s*(10 if b else 1))

for _ in xrange(40):
    s=randint(1,10**randint(2,4))*100; b=[False, True][randint(0,1)]
    Test.it("Testing for %s and %s" %(s,b))
    Test.assert_equals(bonus_time(s,b),sol(s,b),"It should work for random inputs too")
"""