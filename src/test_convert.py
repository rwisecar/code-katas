"""Test for convert.py"""
import pytest


"""
Below are the Code Wars test cases, which I have had to refactor:

Test.assert_equals(digitize(35231),[1,3,2,5,3])
Test.assert_equals(digitize(23582357),[7,5,3,2,8,5,3,2])
Test.assert_equals(digitize(984764738),[8,3,7,4,6,7,4,8,9])
Test.assert_equals(digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
Test.assert_equals(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])

Test.describe('Random tests')
from random import randint
for x in range(37):
    y = randint(10, 99 * 2 ** x)
    Test.it('Testing %s' % y)
    Test.assert_equals(digitize(y), map(int, list(str(y)[::-1])))
"""

CONVERT_PARAMS_TABLE = [
    [(35231), [1, 3, 2, 5, 3]],
    [(23582357), [7, 5, 3, 2, 8, 5, 3, 2]],
    [(984764738), [8, 3, 7, 4, 6, 7, 4, 8, 9]],
    [(45762893920), [0, 2, 9, 3, 9, 8, 2, 6, 7, 5, 4]],
    [(548702838394), [4, 9, 3, 8, 3, 8, 2, 0, 7, 8, 4, 5]]
]


@pytest.mark.parametrize('n, result', CONVERT_PARAMS_TABLE)
def test_convert(n, result):
    """Test for digitize function"""
    from convert import digitize
    assert digitize(n) == result
