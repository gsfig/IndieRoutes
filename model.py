import json
import sqlite3
from os.path import isfile, getsize


def get_poi_db_json() -> dict:
    """

    :return: json of POI database
    """
    list_poi = []

    conn = sqlite3.connect('poi.db')
    c = conn.cursor()
    c2 = conn.cursor()

    sql = '''SELECT id, rating, short_desc, detail_desc, point FROM poi '''
    for id, rating, short_desc, detail_desc, point in c.execute(sql):
        sql_2 = '''SELECT latitude, longitude FROM point WHERE id=(?)'''
        for latitude, longitude in c2.execute(sql_2, str(point), ):
            poi = {"id": id, "rating": rating, "description": short_desc, "details": detail_desc, "latitude": latitude,
                   "longitude": longitude}
            list_poi.append(poi)
    conn.close()
    return {'poi': list_poi}


def get_from_json_file():
    """
    to test
    :return:
    """
    with open("poi_database", "r") as read_file_poi:
        data_poi = json.load(read_file_poi)
    return data_poi


def create_db():
    db_name = 'poi.db'

    if not check_db_file(db_name):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute('DROP TABLE IF EXISTS point')
        c.execute('''CREATE TABLE point(
                        id INTEGER PRIMARY KEY,
                        latitude REAL,
                        longitude REAL)''')

        c.execute('DROP TABLE IF EXISTS poi')
        c.execute('''CREATE TABLE poi(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    rating REAL, 
                    short_desc VARCHAR(255),
                    detail_desc VARCHAR(255),
                    point INTEGER,
                    FOREIGN KEY(point) REFERENCES point(id))''')

        values = [
            (1, 38.7303, -9.1547),
            (2, 38.796855, -9.390765),
            (3, 38.727333, -9.145108),
        ]
        sql = '''INSERT INTO point(id, latitude, longitude) VALUES(?,?,?)'''
        c.executemany(sql, values)

        values = [
            (1, 5, 'Parque Eduardo VII', 'very beautiful garden', 1),
            (2, 7, 'Piriquita', 'descricao dos doces', 2),
            (3, 10, 'Indie Campers', 'Best campervans in the world', 3),
        ]
        sql = '''INSERT INTO poi(id, rating, short_desc, detail_desc, point) VALUES(?,?,?,?,?)'''
        c.executemany(sql, values)

        conn.commit()
        c.close()


def check_db_file(db_file: str):
    """
    checks existence of sqlite database file
    param: db_file sqlite db file path
    :return: True or False
    """
    if isfile(db_file):
        if getsize(db_file) > 100:
            with open(db_file, 'r', encoding="ISO-8859-1") as f:
                header = f.read(100)
                if header.startswith('SQLite format 3'):
                    # print(str(db_file) + " database detected")
                    return True
                else:
                    print(str(db_file) + " file is not SQLite format 3")
                    return False
        else:
            print(str(db_file) + " file is empty")
            return False
    else:
        print(str(db_file) + " file does not exist")
        return False
