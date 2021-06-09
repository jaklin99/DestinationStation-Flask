import pickle
from services.NSDisrubtionsAPI import NSDisrubtionsAPI

import flask
from flask import Flask
from flask import request
from datetime import datetime
import sklearn
from flask_restful import Api, Resource

app = Flask(__name__)
#api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return 'Hello world'



#api.add_resource(NSDisrubtionsAPI, "/disrubtions")


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
     ns = NSDisrubtionsAPI()
     data = ns.getDisrubtions(stationCode='ASD', time='2021-05-26T06:15:00+0200')
     return data


if __name__ == '__main__':
    app.run()
