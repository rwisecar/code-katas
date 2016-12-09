"""Input a string, and return a string with the case of each letter swapped."""


def to_alternating_case(string):
    return "".join([s.swapcase() for s in string])
