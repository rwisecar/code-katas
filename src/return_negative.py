"""Takes a number and, if positive, returns a negative.
If the number was already negative, it returns the number unchanged."""


def make_negative(number):
    """Return the negative of the absolute value of number."""
    return abs(number) * -1
