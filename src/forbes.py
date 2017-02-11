"""Write a function that returns the name, net worth, and industry of:
- the oldest billionaire under 80 years old
- the youngest billionaire with a valid age.
You may not use a sorting function.
"""

import json


def get_json(fpath):
    """Get json data from file."""
    with open(fpath, 'r') as f:
        data = json.load(f)
    return data


def names_and_ages():
    """Compile a dictionary of all billionaires' names and ages."""
    data = get_json('/Users/rachaelwisecarver/codefellows/401/wk1/day5/snowday/code-katas/src/forbes.json')
    age_dict = {}
    for item in data['billionaires']:
        if item['age'] >= 80 or item['age'] < 0:
            pass
        else:
            age_dict[item['name']] = item['age']
    return age_dict


def find_oldest():
    """Find the oldest billionaire under 80."""
    age_dict = names_and_ages()
    return max(age_dict.items(), key=lambda x: x[1])


def find_youngest():
    """Find the youngest billionaire on the list."""
    age_dict = names_and_ages()
    return min(age_dict.items(), key=lambda x: x[1])
