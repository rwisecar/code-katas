"""A function that returns the sum of a series up to the nth value.
The series in question is: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +..."""


def series_sum(n):
    """Returns the sum of a series up to the nth value."""
    total = 0
    if n < 1:
        return '0.00'
    for i in range(1, n + 1):
        total += 1.0 / (3 * i - 2)
        if i == n:
            # 2 decimal place string formatting found on Stack Overflow
            return '{:.2f}'.format(total)
