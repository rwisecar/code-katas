"""This program has two functions, both of which take a list as input.
The first function returns the smallest item in the list.
The second function returns the largest item in that list."""


def mini(lst):
    """Returns the smallest item in an list"""
    if lst:
        return sorted(lst)[0]
    return lst


def maxi(lst):
    """returns the largest item in a list"""
    if lst:
        return sorted(lst)[-1]
    return lst
