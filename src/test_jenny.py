"""Test for jenny.py"""

import pytest

""" Below are the test cases from Code Wars, which I have refactored.
Test.describe("Jenny's greeting function")
Test.it("should greet some people normally")
Test.assert_equals(greet("James"), "Hello, James!")
Test.assert_equals(greet("Jane"), "Hello, Jane!")
Test.assert_equals(greet("Jim"), "Hello, Jim!")

Test.it("should greet Johnny a little bit more special")
Test.assert_equals(greet("Johnny"), "Hello, my love!")
"""

JENNY_PARAMS_TABLE = [
    ["James", "Hello, James!"],
    ["Jane", "Hello, Jane!"],
    ["Jim", "Hello, Jim!"],
    ["Johnny", "Hello, my love!"]
]


@pytest.mark.parametrize("n, result", JENNY_PARAMS_TABLE)
def test_jenny(n, result):
    """test the greet function from the Jenny module"""
    from jenny import greet
    assert greet(n) == result
