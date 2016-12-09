"""Input a string and the function returns that same string with no vowels."""


def disemvowel(string):
    vowels = 'aeiouAEIOU'
    return "".join([c for c in string if c not in vowels])
