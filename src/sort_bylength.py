"""Input an list of strings as an argument and return a sorted array.
The array should be ordered from shortest to longest."""


def sort_by_length(arr):
    """Sort list of strings by length of each string."""
    return sorted(arr, key=len)
