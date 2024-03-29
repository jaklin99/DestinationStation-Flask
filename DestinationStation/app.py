from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import sklearn
import pickle

from services.DataProcesingService import simplifyNsAdvices, join_rides_with_disruptions, add_weather_data, get_model_features, add_predictions
from services.NSRideAdviceAPI import NSRideAdviceAPI
from services.NSDisrubtionsAPI import NSDisrubtionsAPI
from services.WeatherAPI import WeatherAPI


app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/delays": {"origins": "http://localhost:3000"}})

with open('model/MLPRegressor.pickle', 'rb') as file:
    model = pickle.load(file)

advicesApi = NSRideAdviceAPI("de123543b4934bbdaea411ccb85e6a41")
distuptionsApi = NSDisrubtionsAPI("de123543b4934bbdaea411ccb85e6a41")
weatherApi = WeatherAPI("33f1b0b25fe148d68c595356210906")


@app.route('/delays',  methods=['GET'])
def delays():
    departure = request.args.get('departureStation', 'UT')
    destination = request.args.get('destinationStation', 'ASD')
    rideTime = request.args.get(
        'rideTime',
        datetime.now().strftime("%Y-%m-%dT%H:%M")
    )

    rides = simplifyNsAdvices(advicesApi.getAdvice(
        departure, destination, rideTime)['trips']
    )

    disruptions = distuptionsApi.getDisrubtions()

    rides = join_rides_with_disruptions(rides, disruptions)

    weatherASD = weatherApi.getData("Amsterdam")
    weatherUT = weatherApi.getData("Utrecht")

    rides = add_weather_data(rides, weatherUT, weatherASD)

    features = get_model_features(rides)

    predictions = list(model.predict(features))

    rides = add_predictions(rides, predictions)

    return {"rides": rides}


if __name__ == '__main__':
    app.run(debug=True)
