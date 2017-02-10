"""Test flight_paths.py module."""

import pytest
import os
import sys

from flight_paths import get_json, lat_long_dict, create_graph, flight_path


LAT_LONG_PARAMS = [
    ['Victoria Falls', [-18.0958806, 25.8390056]],
    ['Trapani', [37.91194, 12.49333]],
    ['Ferry Reach', [32.36417, -64.67861]],
    ['Salt Lake City', [40.78833, -111.97778]],
    ['Rotterdam', [51.94902, 4.434022]],
    ['Quebec City', [46.79111, -71.39333]],
    ['Puebla', [19.15806, -98.37139]],
    ['Lubumbashi', [-11.5913333, 27.5309778]],
    ['Lilongwe', [-13.78917, 33.78083]],
    ['Kursk', [51.75167, 36.29667]],
    ['Kos Island', [36.7933361, 27.09167]],
    ['Khujand', [40.21528, 69.69472]],
    ['Hassi Messaoud', [31.67222, 6.14028]],
    ['Dar es Salaam', [-6.87806, 39.20278]],
    ['Dallas/Fort Worth', [32.89694, -97.03806]],
]


@pytest.fixture()
def test_graph():
    return create_graph()


def test_get_json():
    """Test that get_json retrieves the correct file and opens as json."""
    flight_data = get_json('/Users/rachaelwisecarver/codefellows/401/wk1/day5/snowday/code-katas/flight_data.json')
    assert flight_data[0]['airport'] == 'Goma International Airport'
    assert flight_data[0]['city'] == 'Goma'
    assert flight_data[0]['destination_cities'] == ['Kinshasa', 'Kisangani', 'Addis Ababa']
    assert len(flight_data) == 741


@pytest.mark.parametrize("n, result", LAT_LONG_PARAMS)
def test_lat_long_dict_returns_correct_distances(n, result):
    """Test that lat_long_dict returns the correct distances for each city."""
    lat_long = lat_long_dict()
    assert lat_long[n] == result


def test_create_graph_creates_graph(test_graph):
    """Test that create_graph actually creates a graph with flight data."""
    assert test_graph.graph['Apia'] == {'Auckland': 1796.4019736705861,
                                        'Brisbane': 2430.9291706927943,
                                        'Honolulu': 2609.724281989286,
                                        'Nadi': 751.7058230300344,
                                        'Suva': 690.7924321944838,
                                        'Sydney': 2686.9975474440935
                                        }
    assert test_graph.graph['London']['New York City'] == 3459.5239201665863


def test_flight_path_base_cases():
    """Test that flight_path returns path, distance between two cities."""
    if sys.version_info[0] == 2:
        assert flight_path('San Francisco', 'Rome') == [
            6429.356344926646, ['San Francisco', u'Victoria', u'Vancouver', u'Rome']]
    else:
        assert flight_path('San Francisco', 'Rome') == [
            6429.356344926646, ['San Francisco', 'Victoria', 'Vancouver', 'Rome']]
    assert flight_path('London', 'Nantes') == 'There is a direct flight from London to Nantes, at 336.942561456 miles.'


def test_flight_path_start_not_in_dict():
    """Test that flight_path raises KeyError if start city is not in dict."""
    with pytest.raises(KeyError):
        flight_path("The Moon", "London")


def test_flight_path_no_connection_to_destination():
    """Test that flight_path raises ValueError if no path to destination."""
    with pytest.raises(ValueError):
        flight_path("London", "The Moon")


def test_flight_path_dest_has_no_lat_or_long():
    """Test for when a destination city has no lat or long."""
    if sys.version_info[0] == 2:
        assert flight_path('Plaine Magnien', 'Hahaya') == "[106363.31814988135, ['Plaine Magnien', u'Dubai', u'Hargeisa', u'Addis Ababa', u'Mombasa', u'Zanzibar', u'Dar es Salaam', u'Hai District', u'Nairobi', u'Hahaya']]. Caution: the distance of this path may be inaccurate due to lack of location data on one or more city."
    else:
        assert flight_path('Plaine Magnien', 'Hahaya') == "[106363.31814988135, ['Plaine Magnien', 'Dubai', 'Hargeisa', 'Addis Ababa', 'Mombasa', 'Zanzibar', 'Dar es Salaam', 'Hai District', 'Nairobi', 'Hahaya']]. Caution: the distance of this path may be inaccurate due to lack of location data on one or more city."