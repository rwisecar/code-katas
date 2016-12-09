"""Takes an integer as input.
Returns the digits of that integer in reverse order in a list."""


def digitize(n):
    """Convert integer to reversed list of digits."""
    stringy = str(n)
    return [int(s) for s in stringy[::-1]]
