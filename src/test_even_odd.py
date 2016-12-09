"""Test for even_odd.py"""
import pytest

"""
These are the original test cases from Code Wars, which I had to refactor.

test.assert_equals(even_or_odd(2), "Even", 'even_or_odd(2)')
test.assert_equals(even_or_odd(1), "Odd", 'even_or_odd(1)')
test.expect(even_or_odd(0) == "Even")
test.expect(even_or_odd(1545452) == "Even")
test.expect(even_or_odd(7) == "Odd")
test.expect(even_or_odd(78) == "Even")
test.expect(even_or_odd(17) == "Odd")
test.expect(even_or_odd(74156741) == "Odd")
test.expect(even_or_odd(100000) == "Even")
"""

EVEN_ODD_PARAMS_TABLE = [
    [2, "Even"],
    [1, "Odd"],
    [0, "Even"],
    [1545452, "Even"],
    [7, "Odd"],
    [78, "Even"],
    [17, "Odd"],
    [74156741, "Odd"],
    [100000, "Even"],
]


@pytest.mark.parametrize('n, result', EVEN_ODD_PARAMS_TABLE)
def test_even_odd(n, result):
    """Test the even/odd function"""
    from even_odd import even_or_odd
    assert even_or_odd(n) == result
