def simplifyNsAdvices(advices):
    return list(map(_simplify_advice, advices))


def _simplify_advice(advice):
    return {
        "departureStation":     advice['legs'][0]['origin']['name'],
        "plannedDepartureTime": advice['legs'][0]['origin']['plannedDateTime'],
        "destinationStation":   advice['legs'][0]['destination']['name'],
        "plannedArrivalTime":   advice['legs'][0]['destination']['plannedDateTime'],
        "rideId":               advice['legs'][0]['product']['number'],
        "trainId":              advice['legs'][0]['product']['number'],
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
                        print(disruption)
                        return ride
    return rides
