"""Test for sort_bylength.py"""

import pytest
from sort_bylength import sort_by_length

SORT_PARAMS_TABLE = [
    [["beg", "life", "i", "to"], ["i", "to", "beg", "life"]],
    [["", "moderately", "brains", "pizza"], ["", "pizza", "brains", "moderately"]],
    [["longer", "longest", "short"], ["short", "longer", "longest"]],
    [["dog", "food", "a", "of"], ["a", "of", "dog", "food"]],
    [["", "dictionary", "eloquent", "bees"], ["", "bees", "eloquent", "dictionary"]],
    [["a longer sentence", "the longest sentence", "a short sentence"], ["a short sentence", "a longer sentence", "the longest sentence"]],
]


@pytest.mark.parametrize("n, result", SORT_PARAMS_TABLE)
def test_sort_bylength(n, result):
    """Test basic use cases for sort_bylength()."""
    assert sort_by_length(n) == result


def test_random_sort():
    """Test random use cases for sort_by_length(), from Code Wars."""
    from random import sample, randint, choice
    from string import ascii_letters

    def generate_test_case():
        return ["".join(choice(ascii_letters) for _ in range(l)) for l in sample(range(1000), randint(0, 100))]
    reference = lambda a: sorted(a, key=len)
    for _ in range(100):
        test_case = generate_test_case()
        assert sort_by_length(test_case) == reference(test_case)


"""Below are the Code Wars test cases which I've refactored.

tests = [
    [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
    [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
    [["short", "longer", "longest"], ["longer", "longest", "short"]],
    [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
    [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
    [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],
]

for exp, inp in tests:
    test.assert_equals(sort_by_length(inp), exp)

test.describe('Random Tests')

from random import sample, randint, choice
from string import ascii_letters

def generate_test_case():
    return [''.join(choice(ascii_letters) for _ in range(l)) for l in sample(range(1000), randint(0, 100))]

reference = lambda a: sorted(a, key=len)

for _ in range(100):
    test_case = generate_test_case()
    test.assert_equals(sort_by_length(test_case), reference(test_case))
"""