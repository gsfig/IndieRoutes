from model import get_poi_db
from openRouteAPI import distance_between_points, get_directions
import json


def get_highlights(lon_origin, lat_origin, lon_destination, lat_destination) -> dict:
    """

    :return: POI highlights closest to route
    """
    min_poi_rating = 7 # should be in config file, rating to be considered highlight
    max_distance_to_route = 10000 # should be in config file, maximum distance (poi - route) in meters for poi to be considered

    list_poi = []

    directions = get_directions(lon_origin, lat_origin, lon_destination, lat_destination)
    route_coords = directions['features'][0]['geometry']['coordinates']

    poi_db = get_poi_db()

    # TODO: check if POI is inside route bounding box to decrease number of POI to check
    # TODO: check if distance between points in route < some value to decrease number of points to check

    for poi in poi_db['poi']:
        if int(poi['rating']) >= min_poi_rating:
            to_add = {'id': poi['id'], 'description' : poi['description']}
            for lon, lat in route_coords:
                if to_add not in list_poi:
                    poi_lat = poi['latitude']
                    poi_lon = poi['longitude']
                    distance_poi_route = distance_between_points(lon, lat, poi_lon, poi_lat)
                    if distance_poi_route <= max_distance_to_route:
                        list_poi.append({'id': poi['id'], 'description' : poi['description']})

    return json.dumps({'poi_highlights' : list_poi})


def get_nearest_poi(longitude: float, latitude: float) -> dict:
    """

    :return: json with nearest POI to given coordinates
    """
    nearest_poi = {}
    shortest_distance = 999
    poi_list = get_poi_db()
    print(poi_list)

    for poi in poi_list['poi']:

        print(poi)
        poi_lat = poi['latitude']
        print('poi_lat: ' + str(poi_lat))
        poi_lon = poi['longitude']
        distance = distance_between_points(poi_lat, poi_lon, latitude, longitude)

        if distance < shortest_distance:
            nearest_poi = poi

    # return nearest_poi
    return {'poi': [{'id': 1, 'name': 'poi_name_nearest'}]}

