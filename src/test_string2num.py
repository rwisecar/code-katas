"""Test string2num.py"""

import pytest
from random import randint

from string2num import string_to_number

STRING_NUMBER_PARAMS_TABLE = [
    ["1234", 1234],
    ["605", 605],
    ["1405", 1405],
    ["-7", -7]
]


@pytest.mark.parametrize("n, result", STRING_NUMBER_PARAMS_TABLE)
def test_string2num(n, result):
    """Test the basic use cases of string_to_number()"""
    assert string_to_number(n) == result


def test_random_string2num():
    """Test the random use cases of string_to_number(), from Code Wars"""
    for i in map(lambda a: randint(1, 50000), range(96)):
        assert string_to_number(str(i)) == i


"""Below are the Code Wars tests, which I've refactored:

test.describe("string_to_number")

test.it("Should work for the examples:")
test.assert_equals( string_to_number("1234"), 1234)
test.assert_equals( string_to_number("605"), 605)
test.assert_equals( string_to_number("1405"), 1405)
test.assert_equals( string_to_number("-7"), -7)

test.it("Should work for random strings:")
for i in map( lambda a: randint(1,50000), range(96)):
    test.assert_equals(string_to_number(str(i)), i)
"""