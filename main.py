from controller import get_highlights, get_nearest_poi
from model import create_db
from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')


@app.route('/get_highlights', methods=['GET'])
def query_highlights():
    form = request.args.to_dict()
    highlights = get_highlights(form['o_lon'], form['o_lat'], form['d_lon'], form['d_lat'])
    print("query: " + str(form['o_lon']) + " " + str(form['o_lat']))
    print('highlightLIST: ' + str(highlights))

    return json.dumps(highlights)


@app.route('/get_closest', methods=['GET'])
def query_closest():
    form = request.args.to_dict()
    nearest_poi = get_nearest_poi(form['lon'], form['lat'])
    print("query: " + str(form['lon']) + " " + str(form['lat']))
    print('nearest_poi: ' + str(nearest_poi))

    return json.dumps(nearest_poi)



# create_db()
# highlight_list = get_highlights(-9.14516, 38.72743, -9.39042, 38.78756)
# print("POI highlights close to route: ")
# print(highlight_list)
#
# print("\n")
#
# nearest_poi = get_nearest_poi(-9.14516, 38.72743)
# print("Closest POI to coordinate: ")
# print(nearest_poi)


# command line
# export FLASK_DEBUG=1
# export FLASK_APP=main.py
# python -m flask run