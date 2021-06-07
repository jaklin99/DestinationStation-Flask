import pickle
from controllers.DisrubtionsController import DisrubtionsController

import flask
from flask import Flask
from flask import request
from datetime import datetime
import sklearn
app = Flask(__name__)


with open('model/MLPRegressor.pickle', 'rb') as file:
     model = pickle.load(file)


# /delays?departureStation=ASD&destinationStation=UT&rideTime=2021-06-31T13:59
@app.route('/delays',  methods=['GET'])
def delays():
    departure = request.args.get('departureStation', 'UT')
    destination = request.args.get('destinationStation', 'ASD')
    rideTime = request.args.get(
        'rideTime',
        datetime.now().strftime("%Y-%m-%dT%H:%M")
    )

    return 'Hello World!'


@app.route('/disrubtions',  methods=['GET'])
def disrubtions():
     data = DisrubtionsController.getDisrubtions('15:15','ASD')
     return data


if __name__ == '__main__':
    app.run()
