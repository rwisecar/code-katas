"""A function that, given a starting city and destination city, returns:
1. A path between the cities, and
2. The distance from one city to the next.
"""
import json
import os
from flight_graph import Graph


def get_json(fpath):
    """Get json data from file."""
    with open(fpath, 'r') as f:
        flight_data = json.load(f)
    return flight_data


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(
        0.5 * delta_phi)**2 + math.cos(
        phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def lat_long_dict():
    """Find each city's latitude and longitude and save in a dictionary."""
    flight_data = get_json('/Users/rachaelwisecarver/codefellows/401/wk1/day5/snowday/code-katas/flight_data.json')
    lat_long = {}
    for item in flight_data:
        lat_long[item['city']] = item['lat_lon']
    return lat_long


def create_graph():
    """Put json data into a weighted graph data structure.
    If the city is included in destination_cities, but not as a city in its own
    right, make the weight excessively long. This way, the path will still show
    up, but the route will not be favored when calculating the shortest flight
    path.
    """
    flight_data = get_json('/Users/rachaelwisecarver/codefellows/401/wk1/day5/snowday/code-katas/flight_data.json')
    lat_long = lat_long_dict()
    connections = Graph()
    for item in flight_data:
        start = item['city']
        for destination in item['destination_cities']:
            if destination in list(lat_long.keys()):
                connections.add_edge(
                    start, destination, calculate_distance(
                        lat_long[start], lat_long[destination]))
            connections.add_edge(
                start, destination, 500000)
    return connections


def flight_path(start, dest):
    """Return the shortest routes between two cities."""
    connections = create_graph()
    unvisited = connections.depth_traversal(start)
    if start not in unvisited:
        raise KeyError("That city is not in the database.")
    elif dest not in unvisited:
        raise ValueError("There is no connection between those cities.")
    else:
        path = connections.dijkstra(start, dest)
        if path.keys() > 500000:
            return "There is a path between those cities, but the distance is unknown."
        else:
            return path
