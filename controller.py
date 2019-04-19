from model import get_poi_db


def get_highlights(lon_start: float, lat_start: float, lon_end: float, lat_end: float) -> dict:
    """

    :return: json with POI highlights closest to route
    """

    max_distance = 10
    poi_list = {}
    route = get_route_coordinates(lon_start, lat_start, lon_end, lat_end)

    for point_route in route:

        poi_list = get_poi_db()
        for poi in poi_list:

            distance_to_route = get_distance(poi['latitude'], poi['longitude'], point_route['latitude'], point_route['longitude'])
            if distance_to_route < max_distance:
                poi_list.update(poi)

    return {'poi': [{'id': 1, 'name': 'poi_name_highlight'}]}


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
        distance = get_distance(poi_lat, poi_lon, latitude, longitude)

        if distance < shortest_distance:
            nearest_poi = poi

    # return nearest_poi
    return {'poi': [{'id': 1, 'name': 'poi_name_nearest'}]}


def get_distance(poi_lat, poi_lon, latitude, longitude):
    return 1


def get_route_coordinates(lon_start, lat_start, lon_end, lat_end):
    return {}
