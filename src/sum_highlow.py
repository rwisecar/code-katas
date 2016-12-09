"""Input a list of numbers.
Remove the highest and lowest values (not indeces) from that list.
Then, return the sum of the remaining numbers in the list.
If the list is empty, null or None, or if only 1 Element exists, return 0."""


def sum_array(arr):
    if arr and arr > 1:
        return sum(sorted(arr)[1:-1])
    return 0
