"""Find the next perfect square of any perfect square input.
If the input is not a perfect square, it will return -1."""

import math


def find_next_square(sq):
    root = math.sqrt(sq)
    if root == round(root):
        return (root + 1) ** 2
    else:
        return -1
