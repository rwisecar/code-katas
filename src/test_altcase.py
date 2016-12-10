"""Test for alt_case.py"""

import pytest
from alt_case import to_alternating_case

ALTCASE_PARAMS_TABLE = [
    ["altERnaTIng cAsE", "ALTerNAtiNG CaSe"],
    ["ALTerNAtiNG CaSe", "altERnaTIng cAsE"],
    ["hello world", "HELLO WORLD"],
    ["HELLO WORLD", "hello world"],
    ["hello WORLD", "HELLO world"],
    ["HeLLo WoRLD", "hEllO wOrld"],
    ["12345", "12345"],
    ["1a2b3c4d5e", "1A2B3C4D5E"],
    ["String.prototype.toAlternatingCase", "sTRING.PROTOTYPE.TOaLTERNATINGcASE"],
]


@pytest.mark.parametrize("n, result", ALTCASE_PARAMS_TABLE)
def test_altcase(n, result):
    """Tests the basic use cases of to_alternate_case()."""
    assert to_alternating_case(n) == result


def test_random_altcase():
    """Tests random use cases of to_alternate_case(), from Code Wars."""
    from random import randint
    sol = lambda s: "".join([x.lower() if x == x.upper() else x.upper() for x in s])
    base = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 .,;:!?/"
    for _ in range(40):
        s = "".join(base[randint(0, len(base)-1)] for x in range(randint(1, 30)))
        assert to_alternating_case(s) == sol(s)


""" Below are the Code Wars test cases, which I refactored above:

Test.describe("Basic tests")
Test.it("should work for fixed tests (provided in the description)")
Test.assert_equals(to_alternating_case("hello world"), "HELLO WORLD")
Test.assert_equals(to_alternating_case("HELLO WORLD"), "hello world")
Test.assert_equals(to_alternating_case("hello WORLD"), "HELLO world")
Test.assert_equals(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")
Test.assert_equals(to_alternating_case("12345"), "12345")
Test.assert_equals(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")
Test.assert_equals(to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")
Test.assert_equals(to_alternating_case(to_alternating_case("Hello World")), "Hello World")
Test.it("should work for the title of this Kata")
title = "altERnaTIng cAsE"
title = to_alternating_case(title)
Test.assert_equals(title, "ALTerNAtiNG CaSe")
title = to_alternating_case(title)
Test.assert_equals(title, "altERnaTIng cAsE")
title = to_alternating_case(title)
Test.assert_equals(title, "ALTerNAtiNG CaSe")
title = to_alternating_case(title)
Test.assert_equals(title, "altERnaTIng cAsE")
title = "altERnaTIng cAsE <=> ALTerNAtiNG CaSe"
title = to_alternating_case(title)
Test.assert_equals(title, "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
title = to_alternating_case(title)
Test.assert_equals(title, "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")
title = to_alternating_case(title)
Test.assert_equals(title, "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
title = to_alternating_case(title)
Test.assert_equals(title, "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")

Test.describe("Random tests")
from random import randint
sol=lambda s: "".join([x.lower() if x==x.upper() else x.upper() for x in s])
base="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 .,;:!?/"

for _ in xrange(40):
  s="".join(base[randint(0,len(base)-1)] for x in xrange(randint(1,30)))
  Test.it("Testing for %s" %repr(s))
  Test.assert_equals(to_alternating_case(s), sol(s), "It should work for random inputs too")
"""
