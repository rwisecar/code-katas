"""Input a string, and return a string with each word reversed.
The original order of each word in the string should remain.
White space should also be maintained."""


def reverse_words(str):
    return " ".join(["".join(s[::-1]) for s in str.split(" ")])
