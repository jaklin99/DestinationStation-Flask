import requests


class NSRideAdviceAPI:

    def __init__(self, key) -> None:
        self.key = key

    def getAdvice(self, origin, destination, time):
        url = 'https://gateway.apiportal.ns.nl/reisinformatie-api/api/v3/trips?' +\
            f'fromStation={origin}&toStation={destination}&originWalk=false&originBike=false&originCar=false&destinationWalk=false&destinationBike=false&destinationCar=false' +\
            f'&dateTime={time}&shorterChange=false&travelAssistance=false&searchForAccessibleTrip=false&localTrainsOnly=false&excludeHighSpeedTrains=false' +\
            '&excludeTrainsWithReservationRequired=false&yearCard=false&discount=NO_DISCOUNT&travelClass=2&polylines=false&passing=false&travelRequestType=DEFAULT'

        request = requests.get(
            url, headers={"Ocp-Apim-Subscription-Key": self.key}
        )

        return request.json()
