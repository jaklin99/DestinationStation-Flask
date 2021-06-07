from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)


# /delays?departureStation=ASD&destinationStation=UT&rideTime=2021-06-31T13:59
@app.route('/delays',  methods=['GET'])
def hello_world():
    departure = request.args.get('departureStation', 'UT')
    destination = request.args.get('destinationStation', 'ASD')
    rideTime = request.args.get(
        'rideTime',
        datetime.now().strftime("%Y-%m-%dT%H:%M")
    )
    print(departure, destination, rideTime)

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
