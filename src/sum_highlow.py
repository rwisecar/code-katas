"""Input a list of numbers."""


def sum_array(arr):
    if arr and len(arr) > 1:
        return sum(sorted(arr)[1:-1])
    return 0
