"""Test for get_grade.py"""

import pytest
import random
from get_grade import get_grade


GRADE_PARAMS_TABLE = [
    [95, 90, 93, "A"],
    [100, 85, 96, "A"],
    [92, 93, 94, "A"],
    [100, 100, 100, "A"],
    [70, 70, 100, "B"],
    [82, 85, 87, "B"],
    [84, 79, 85, "B"],
    [70, 70, 70, "C"],
    [75, 70, 79, "C"],
    [60, 82, 76, "C"],
    [65, 70, 59, "D"],
    [66, 62, 68, "D"],
    [58, 62, 70, "D"],
    [44, 55, 52, "F"],
    [48, 55, 52, "F"],
    [58, 59, 60, "F"],
    [0, 0, 0, "F"],
]


@pytest.mark.parametrize("s, t, u, result", GRADE_PARAMS_TABLE)
def test_get_grade(s, t, u, result):
    """Test basic use cases for get_grade()."""
    assert get_grade(s, t, u) == result


def test_random_grades():
    """Test random use cases for get_grade()."""
    for i in range(100):
        rand1 = random.randint(0, 100)
        rand2 = random.randint(0, 100)
        rand3 = random.randint(0, 100)
        assert get_grade(rand1, rand2, rand3) == solution(rand1, rand2, rand3)


def solution(s1, s2, s3):
    """Test case provided by Code Wars for the test_random_grades fcn."""
    s = (s1 + s2 + s3) / 3
    if s >= 90:
        return "A"
    if s >= 80:
        return "B"
    if s >= 70:
        return "C"
    if s >= 60:
        return "D"
    return "F"


""" Below are the Code Wars' test cases, which I've refactored above.

test.describe("grade book")
test.it("should return an A")
test.assert_equals(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
test.assert_equals(get_grade(100, 85, 96), "A", "get_grade(100, 85, 96)")
test.assert_equals(get_grade(92, 93, 94), "A", "get_grade(92, 93, 94)")
test.assert_equals(get_grade(100, 100, 100), "A", "get_grade(100, 100, 100)")

test.it("should return a B")
test.assert_equals(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
test.assert_equals(get_grade(82, 85, 87), "B", "get_grade(82, 85, 87)")
test.assert_equals(get_grade(84, 79, 85), "B", "get_grade(84, 79, 85)")

test.it("should return a C")
test.assert_equals(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
test.assert_equals(get_grade(75, 70, 79), "C", "get_grade(75, 70, 79)")
test.assert_equals(get_grade(60, 82, 76), "C", "get_grade(60, 82, 76)")

test.it("should return a D")
test.assert_equals(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
test.assert_equals(get_grade(66, 62, 68), "D", "get_grade(66, 62, 68)")
test.assert_equals(get_grade(58, 62, 70), "D", "get_grade(58, 62, 70)")

test.it("should return an F")
test.assert_equals(get_grade(44, 55, 52), "F", "get_grade(44, 55, 52)")
test.assert_equals(get_grade(48, 55, 52), "F", "get_grade(48, 55, 52)")
test.assert_equals(get_grade(58, 59, 60), "F", "get_grade(58, 59, 60)")
test.assert_equals(get_grade(0, 0, 0), "F", "get_grade(0, 0, 0)")

def solution(s1, s2, s3):
    s = (s1 + s2 + s3) / 3
    if s >= 90: return "A"
    if s >= 80: return "B"
    if s >= 70: return "C"
    if s >= 60: return "D"
    return "F"
    
test.it("should work for random numbers")
for i in range(100):
    rand1 = random.randint(0, 100)
    rand2 = random.randint(0, 100)
    rand3 = random.randint(0, 100)
    test.assert_equals(get_grade(rand1, rand2, rand3), solution(rand1, rand2, rand3))
"""