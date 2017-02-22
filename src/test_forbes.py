# -*- coding: UTF-8 -*-
"""Test forbes.py module."""

import pytest
from forbes import get_json, oldest_youngest


def test_that_get_json_loads_file():
    """Test that get_json method loads the file."""
    data = get_json()
    assert data['billionaires'][0]['name'] == "Bill Gates"
    assert data['billionaires'][-1]['name'] == "Paul Allen"


def test_that_find_oldest_returns_oldest_under_80():
    """Test that find_oldest returns the oldest person under 80."""
    assert oldest_youngest() == ((u'Phil Knight', {
        'age': 78, 'industry': u'Nike', 'net worth': 24400000000}),
        (u'Mark Zuckerberg', {
            'age': 32, 'industry': u'Facebook', 'net worth': 44600000000}))
