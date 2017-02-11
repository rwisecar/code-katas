"""Test forbes.py module."""

import pytest
from forbes import get_json, names_and_ages, find_oldest, find_youngest


def test_that_get_json_loads_file():
    """Test that get_json method loads the file."""
    data = get_json('/Users/rachaelwisecarver/codefellows/401/wk1/day5/snowday/code-katas/src/forbes.json')
    assert data['billionaires'][0]['name'] == "Bill Gates"
    assert data['billionaires'][-1]['name'] == "Paul Allen"


def test_that_names_and_ages_returns_parsed_dict():
    """Test that names_and_ages method returns a dict w/p ppl > 80 and < 0."""
    test_dict = names_and_ages()
    assert "Maria Franca Fissolo" not in list(test_dict.keys())
    assert "Beate Heister & Karl Albrecht Jr." not in list(test_dict.keys())
    assert "Georg Schaeffler" in list(test_dict.keys())


def test_that_find_oldest_returns_oldest_under_80():
    """Test that find_oldest returns the oldest person under 80."""
    assert find_oldest() == (u'Phil Knight', 78)


def test_that_find_youngest_returns_youngest_valid_billionaire():
    """Test that find_oldest returns the youngest person actually born."""
    assert find_youngest() == (u'Mark Zuckerberg', 32)
