"""Find the next perfect square of any perfect square input.
If the input is not a perfect square, it will return -1."""

import math


def find_next_square(sq):
    """If perfect square input, return next perfect square. Else return -1."""
    root = math.sqrt(sq)
    if root == round(root):
        return (root + 1) ** 2
    else:
        return -1
