import requests
from geopy import distance
import json


def get_directions(lon_origin, lat_origin, lon_destination, lat_destination) -> dict:
    """
    Change to have openrouteservice API working
    """
    return get_directions_simple(lon_origin, lat_origin, lon_destination, lat_destination)
    # return get_directions_withAPI(lon_origin, lat_origin, lon_destination, lat_destination)


def distance_between_points(lon, lat, poi_lon, poi_lat) -> float:
    """
    Change to have openrouteservice API working
    API Rate limit exceeds with too many requests

    """
    return distance_between_points_simple(lon, lat, poi_lon, poi_lat)
    # return distance_between_points_withAPI(lon, lat, poi_lon, poi_lat)


def get_directions_withAPI(lon_origin, lat_origin, lon_destination, lat_destination) -> dict:
    start = str(lon_origin) + ',' + str(lat_origin)
    end = str(lon_destination) + ',' + str(lat_destination)

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    params = (
        ('api_key', '5b3ce3597851110001cf6248008ff000490d4c1486b82b2ceeefdc06'),
        ('start', start),
        ('end', end),
    )

    r = requests.get('https://api.openrouteservice.org/v2/directions/driving-car', params=params, headers=headers)
    j = json.loads(r.text)
    return j


def get_directions_simple(lat_start, lon_start, lat_end, lon_end) -> dict:
    """
    returns same response as API
    for points: -9.14516, 38.72743; -9.39042, 38.78756
    """
    with open("jsonOpenrouteResponse", "r") as read_file_route:
        j = json.load(read_file_route)
        return j


def distance_between_points_withAPI(lon, lat, poi_lon, poi_lat) -> float:
    data_route = get_directions(lon, lat, poi_lon, poi_lat)
    distance_in_m = data_route['features'][0]['properties']['summary']['distance']
    return distance_in_m


def distance_between_points_simple(lon, lat, poi_lon, poi_lat) -> float:
    """
    calculates GeodesicDistance between points.
    Less accurate than distance_between_points() but doesn't have to use API

    :return: distance in meters
    """
    return distance.distance((lat, lon), (poi_lat, poi_lon)).m
