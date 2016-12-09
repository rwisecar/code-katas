"""Input an array of strings as an argument and return a sorted array.
The array should be ordered from shortest to longest."""


def sort_by_length(arr):
    return sorted(arr, key=len)
