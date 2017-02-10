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
                start, destination, 100000)
    return connections


def flight_path(start, dest, checked=None):
    """Find a path and distance between given start and destination cities."""
    connections = create_graph()
    unvisited = connections.depth_traversal(start)
    path = {i: [None, [None]] for i in unvisited}
    path[start] = [0, [start]]

    if start not in unvisited:
        raise KeyError("That city is not in the database.")
    elif dest not in unvisited:
        raise ValueError("There is no connection between those cities.")
    elif dest in connections.graph[start]:
        return "There is a direct flight from {} to {}, at {} miles.".format(start, dest, connections.graph[start][dest])

    current = start
    while unvisited:
        for city in connections.neighbors(current):
            current_distance = path[current][0]
            try:
                distance_to_city = connections.graph[current][city]
            except TypeError:
                continue
            original_distance = path[city][0]

            if city not in unvisited:
                continue
            elif original_distance is None or distance_to_city < original_distance:
                test_path = (path[current])[1][:]
                test_path.append(city)
                try:
                    path[city][0] = distance_to_city + current_distance
                    path[city][1] = test_path
                except TypeError:
                    continue
                continue

        if current == dest:
            if path[dest][0] > 100000 or path[dest] == [None, [None]]:
                return "{}. Caution: the distance of this path may be inaccurate due to lack of location data on one or more city.".format(path[dest])
            return path[dest]

        unvisited.remove(current)
        next_node = None
        for key, value in path.items():
            if key in unvisited:
                if next_node is None:
                    next_node = key
                    continue
                elif path[key][0]:
                    if path[key][0] < path[next_node][0]:
                        next_node = key
        current = next_node
