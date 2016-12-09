"""Input an array of numbers, return the sum of all of the positives ones."""


def positive_sum(arr):
    if arr:
        return sum([a for a in arr if a > 0])
    return 0
