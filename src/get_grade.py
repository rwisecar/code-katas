"""Input 3 test grades, and return a letter grade based on average grade."""


def get_grade(s1, s2, s3):
    avg_grade = (s1 + s2 + s3) / 3
    if avg_grade >= 90:
        return 'A'
    elif avg_grade >= 80:
        return 'B'
    elif avg_grade >= 70:
        return 'C'
    elif avg_grade >= 60:
        return 'D'
    return "F"
