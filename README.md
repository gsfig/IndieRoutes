# IndieRoutes


## Prerequisites
- The use of virtualenv or similar is advisable
    - tested with python3.6
- pip install flask
- pip install geopy
- pip install requests

## Running
- Run Flask:
    - export FLASK_APP=main.py
    - python -m flask run
    
-  API:
    - Go to http://127.0.0.1:5000 for simple UI
    - Or:
        - http://127.0.0.1:5000/get_highlights?o_lon=-9.14516&o_lat=38.72743&d_lon=-9.39042&d_lat=38.78756&form_id=60409&_=1555676741389
        - http://127.0.0.1:5000/get_closest?lon=-9.14516&lat=38.72743&form_id=60409&_=1555684031680
## Build with
- [Geopy](https://github.com/geopy/geopy) to calculate distances without an external API
- [flask](http://flask.pocoo.org/) webservice
- [OpenRouteService](https://openrouteservice.org) external API to calculate routes