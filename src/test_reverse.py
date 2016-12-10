"""Test for reverse.py"""

import pytest
from reverse import reverse_words

REVERSE_PARAMS_TABLE = [
    ['The quick brown fox jumps over the lazy dog.', 'ehT kciuq nworb xof spmuj revo eht yzal .god'],
    ['apple', 'elppa'],
    ['a b c d', 'a b c d'],
    ['double  spaced  words', 'elbuod  decaps  sdrow']
]


@pytest.mark.parametrize("n, result", REVERSE_PARAMS_TABLE)
def test_reverse(n, result):
    """Basic test cases for reverse_words function."""
    assert reverse_words(n) == result


"""Below are the original Code Wars test cases, which I have refactored.
test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'),'ehT kciuq nworb xof spmuj revo eht yzal .god');
test.assert_equals(reverse_words('apple'),'elppa');
test.assert_equals(reverse_words('a b c d'),'a b c d');
test.assert_equals(reverse_words('double  spaced  words'),'elbuod  decaps  sdrow');
"""
