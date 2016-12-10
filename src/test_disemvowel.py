"""Test for disemvowel.py"""

import pytest
from disemvowel import disemvowel

DISEMVOWEL_PARAMS_TABLE = [
    ["This website is for losers LOL!", "Ths wbst s fr lsrs LL!"],
    ["No offense but,\nYour writing is among the worst I've ever read", "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"],
    ["What are you, a communist?", "Wht r y,  cmmnst?"]
]


@pytest.mark.parametrize('n, result', DISEMVOWEL_PARAMS_TABLE)
def test_disemvowel(n, result):
    """Run basic test cases for disemvowel()."""
    assert disemvowel(n) == result


""" Below are the Code Wars tests that I refactored.
tests = [("This website is for losers LOL!", "Ths wbst s fr lsrs LL!"),
         ("No offense but,\nYour writing is among the worst I've ever read", "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"),
         ("What are you, a communist?", "Wht r y,  cmmnst?")]

for case in tests:
    test.assert_equals(disemvowel(case[0]), case[1])
"""
