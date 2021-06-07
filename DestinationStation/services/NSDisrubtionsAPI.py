import requests


class NSDisrubtionsAPI:

    def __init__(self, key) -> None:
        self.key = 'de123543b4934bbdaea411ccb85e6a41'

    def getDisrubtion(stationCode):
        url = f'https://gateway.apiportal.ns.nl/reisinformatie-api/api/v3/disruptions/station/{stationCode}'
        print(url)

        request = requests.get(
            url, headers={"Ocp-Apim-Subscription-Key": 'de123543b4934bbdaea411ccb85e6a41'}
        )

        return request.json()
