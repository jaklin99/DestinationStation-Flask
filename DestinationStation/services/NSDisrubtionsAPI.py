import requests

class NSDisrubtionsAPI:

    def __init__(self) -> None:
        self.key = 'de123543b4934bbdaea411ccb85e6a41'

    def getDisrubtions(self, stationCode, time):
        url = f'https://gateway.apiportal.ns.nl/reisinformatie-api/api/v3/disruptions?type=MAINTENANCE'
        request = requests.get(
            url, headers={"Ocp-Apim-Subscription-Key": self.key}
        )
        data = request.json()
        d = 0                                                                             #used to iterate over the data
        for record in data:
            for delay in data[d]['publicationSections'][0]['section']['stations']:      #iterates over every station mentioned in the data
             if delay['stationCode'] == stationCode:
                 if data[d]['end'] > time > data[d]['start']:                           #format of time is e.g. '2021-05-26T06:15:00+0200'
                     return '1'
            d = d+1
        return '0'

