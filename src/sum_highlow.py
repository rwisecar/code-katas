"""Input list of numbers, return a sum of the list minus min and max values."""


def sum_array(arr):
    """Return a the sum of a list of numbers, minus the min and max values"""
    if arr and len(arr) > 1:
        return sum(sorted(arr)[1:-1])
    return 0
