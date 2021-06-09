import requests


class NSDisrubtionsAPI:

    def __init__(self, key) -> None:
        self.key = key

    def getDisrubtions(self, stationCodes, rides):
        url = f'https://gateway.apiportal.ns.nl/reisinformatie-api/api/v3/disruptions?type=MAINTENANCE'
        request = requests.get(
            url, headers={"Ocp-Apim-Subscription-Key": self.key}
        )
        return request.json()
