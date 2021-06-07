def simplifyNsAdvices(advices):
    return list(map(_simplify_advice, advices))


def _simplify_advice(advice):
    return {
        "departureStation":     advice['legs'][0]['origin']['name'],
        "plannedDepartureTime": advice['legs'][0]['origin']['plannedDateTime'],
        "destinationStation":   advice['legs'][0]['destination']['name'],
        "plannedAeeivalTime":   advice['legs'][0]['destination']['plannedDateTime'],
        "rideId":               advice['legs'][0]['product']['number'],
        "trainId":              advice['legs'][0]['product']['number'],
        "punctuality":          advice['punctuality'] if 'punctuality' in advice else None,
        "nsUrl":                advice['shareUrl']['uri'] if 'shareUrl' in advice else None,
        "crowdForecast":        advice['crowdForecast'] if 'crowdForecast' in advice else 'UNKNOWN',
    }
