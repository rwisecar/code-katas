# -*- coding: UTF-8 -*-
"""Write a function that returns the name, net worth, and industry of:
- the oldest billionaire under 80 years old
- the youngest billionaire with a valid age.
You may not use a sorting function.
"""

import json

FPATH = '/Users/rachaelwisecarver/codefellows/401/wk1/day5/snowday/code-katas/src/forbes.json'


def get_json():
    """Get json data from file."""
    with open(FPATH, 'r') as f:
        data = json.load(f)
    return data


def oldest_youngest():
    """Get JSON Data.
    Compile a dictionary of all billionaires' names and ages.
    Find the oldest billionaire under 80, and youngest living billionaire."""
    data = get_json()
    age_dict = {}
    for item in data['billionaires']:
        if item['age'] >= 80 or item['age'] < 0:
            pass
        else:
            age_dict[item['name']] = {"age": item['age'],
                                      "industry": item['source'],
                                      "net worth": item["net_worth (USD)"]
                                      }
    oldest = max(age_dict.items(), key=lambda x: x[1]["age"])
    youngest = min(age_dict.items(), key=lambda x: x[1]["age"])

    return oldest, youngest
