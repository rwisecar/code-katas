"""Return the sum of a series up to the nth value.
The series in question is: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16, and so on."""


def series_sum(n):
    """Returns the sum of a series up to the nth value."""
    total = 0
    for i in range(n):
        # Math (and revised math) from Stack Overflow
        total += 1 / (1 + 3 * float(i))
    return '{:.2f}'.format(total)
