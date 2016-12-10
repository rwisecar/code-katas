"""Input a string, and return a string with the case of each letter swapped."""


def to_alternating_case(string):
    """Input a string, return string with case swapped"""
    return "".join([s.swapcase() for s in string])
