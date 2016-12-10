"""Input a string, and return a string with each word reversed.
The original order of each word in the string should remain.
White space should also be maintained."""


def reverse_words(str):
    """Reverse the order of letters in each word in a string."""
    return " ".join(["".join(s[::-1]) for s in str.split(" ")])
