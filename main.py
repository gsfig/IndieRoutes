from controller import get_highlights, get_nearest_poi
from model import create_db
from flask import Flask, render_template, request
import json


app = Flask(__name__)
create_db()


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')


@app.route('/get_highlights', methods=['GET'])
def query_highlights():
    form = request.args.to_dict()
    highlights = get_highlights(form['o_lon'], form['o_lat'], form['d_lon'], form['d_lat'])

    return json.dumps(highlights)


@app.route('/get_closest', methods=['GET'])
def query_closest():
    form = request.args.to_dict()
    nearest_poi = get_nearest_poi(form['lon'], form['lat'])

    return json.dumps(nearest_poi)

# command line
# export FLASK_DEBUG=1
# export FLASK_APP=main.py
# python -m flask run
