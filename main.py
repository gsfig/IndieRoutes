from controller import get_highlights, get_nearest_poi
from model import create_db
from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')


@app.route('/sendQuery', methods=['GET'])
def query():
    query_text = request.args.to_dict()
    print('QUERY: ' + str(query_text))

    return json.dumps({'poi': [{'id': 1, 'name': 'sendquery'}]})


create_db()
highlight_list = get_highlights(-9.14516, 38.72743, -9.39042, 38.78756)
print("POI highlights close to route: ")
print(highlight_list)

print("\n")

nearest_poi = get_nearest_poi(-9.14516, 38.72743)
print("Closest POI to coordinate: ")
print(nearest_poi)


# command line
# export FLASK_DEBUG=1
# export FLASK_APP=main.py
# python -m flask run