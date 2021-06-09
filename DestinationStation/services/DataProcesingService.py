import math


def simplifyNsAdvices(advices):
    return list(map(_simplify_advice, advices))


def _simplify_advice(advice):
    return {
        "departureStation":     advice['legs'][0]['origin']['name'],
        "plannedDepartureTime": advice['legs'][0]['origin']['plannedDateTime'],
        "departureHour":        int(advice['legs'][0]['origin']['plannedDateTime'][11:13]),
        "departureDate":        advice['legs'][0]['origin']['plannedDateTime'][0:10],
        "departureStationCode": 1 if advice['legs'][0]['origin'] == 'Utrecht Centraal' else 0,
        "destinationStation":   advice['legs'][0]['destination']['name'],
        "destinationStationCode": 1 if advice['legs'][0]['origin'] == 'Utrecht Centraal' else 0,
        "plannedArrivalTime":   advice['legs'][0]['destination']['plannedDateTime'],
        "arrivalHour":          int(advice['legs'][0]['destination']['plannedDateTime'][11:13]),
        "arrivalDate":          advice['legs'][0]['destination']['plannedDateTime'][0:10],
        "rideId":               int(advice['legs'][0]['product']['number']),
        "trainId":              int(advice['legs'][0]['product']['number']),
        "punctuality":          advice['punctuality'] if 'punctuality' in advice else None,
        "nsUrl":                advice['shareUrl']['uri'] if 'shareUrl' in advice else None,
        "crowdForecast":        advice['crowdForecast'] if 'crowdForecast' in advice else 'UNKNOWN',
    }


def join_rides_with_disruptions(rides, disruptions):
    for ride in rides:
        ride['disruption'] = False

        for disruption in disruptions:
            if 'publicationSections' not in disruption:
                continue
            if disruption['start'] < ride['plannedArrivalTime'] and disruption['end'] > ride['plannedDepartureTime']:
                for delay in disruption['publicationSections'][0]['section']['stations']:
                    if delay['stationCode'] in ['UT', 'ASD']:
                        ride['disruption'] = True
    return rides


def add_weather_data(rides, utrecht, amsterdam):
    if rides[0]['departureStation'] == 'Amsterdam Centraal':
        departures, destinations = amsterdam, utrecht
    else:
        departures, destinations = utrecht, amsterdam

    for ride in rides:
        for dep in departures:
            if dep['date'] == ride['departureDate'] and dep['hour'] == ride['departureHour']:
                for key in dep:
                    ride['departure_'+key] = dep[key]

        for dest in destinations:
            if dest['date'] == ride['arrivalDate'] and dest['hour'] == ride['arrivalHour']:
                for key in dest:
                    ride['destination_'+key] = dest[key]

        for key in ['departure_', 'destination_']:
            if key + 'windspeed' not in ride:
                ride[key+'windspeed'] = 4.3
                ride[key+'visibility'] = 68
                ride[key+'fog'] = 0
                ride[key+'rain'] = 0
                ride[key+'snow'] = 0
                ride[key+'thunder'] = 0
                ride[key+'ice'] = 0

    return rides


def get_model_features(rides):
    features = []
    for ride in rides:
        values = []
        for key in ['rideId', 'trainId', 'departureStationCode', 'destinationStationCode', 'arrivalHour', 'departureHour',
                    'departure_windspeed', 'departure_visibility', 'departure_fog', 'departure_rain', 'departure_snow', 'departure_thunder', 'departure_ice',
                    'destination_windspeed', 'destination_visibility', 'destination_fog', 'destination_rain', 'destination_snow', 'destination_thunder', 'destination_ice',
                    'disruption']:
            values.append(ride[key])
        features.append(values)
    return features


def add_predictions(rides, predictions):
    for ride, pred in zip(rides, predictions):
        ride['arrivalDelay'] = {
            "predictedDelay": round(pred, 1),
            "lowerConfidenceBound": max(0, round(pred - 3, 1)),
            "upperConfidenceBound": round(pred + 3, 1),
            "confidencelevel": 95
        }
    return rides
