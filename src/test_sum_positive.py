"""Tests sum_positive module"""

import pytest

""" Here are Code Wars' test, which I refactor below.
Test.describe("positive_sum")

Test.it("works for some examples")
Test.assert_equals(positive_sum([1,2,3,4,5]),15)
Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

Test.it("returns 0 when array is empty")
Test.assert_equals(positive_sum([]),0)

Test.it("returns 0 when all elements are negative")
Test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)
"""

SUM_POSITIVE_PARAMS_TABLE = [
    [[1, 2, 3, 4, 5], 15],
    [[1, -2, 3, 4, 5], 13],
    [[-1, 2, 3, 4, -5], 9],
    [[], 0],
    [[-1, -2, -3, -4, -5], 0]
]


@pytest.mark.parametrize('n, result', SUM_POSITIVE_PARAMS_TABLE)
def test_sum_pos_params(n, result):
    """Test positive sum function against example lists"""
    from sum_positive import positive_sum
    assert positive_sum(n) == result
