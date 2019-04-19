import json


def create_db():
    print("create_bd")


def get_poi_db():
    return get_poi_from_file()


def get_poi_from_file():
    """
    to test
    :return:
    """
    with open("poi_database_fake", "r") as read_file_poi:
        data_poi = json.load(read_file_poi)

    # print(data_poi)
    return data_poi
