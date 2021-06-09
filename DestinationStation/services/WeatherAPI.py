import requests

class WeatherAPI:

    #def getData(self, station):
        url = f'http://api.weatherapi.com/v1/forecast.json?key=33f1b0b25fe148d68c595356210906&q=Utrecht&days=10&aqi=no&alerts=no'
        request = requests.get(
            url
        )
        data = request.json()

        dictionaries = []
        fogCodes = [1135, 1147, 1030]
        thunderCodes = [1087, 1276, 1282,1273, 1279]
        iceCodes = [1072, 1117, 1168, 1171, 1237, 1264, 1261]

        for record in data['forecast']['forecastday']:
            for hour in record['hour']:
                 windspeed = hour['wind_kph']/36*100
                 visibility = hour['vis_km']
                 code = hour['condition']['code']
                 if visibility < 5:
                     visibility = visibility*10
                 elif visibility == 5:
                     visibility = 50
                 else:
                     visibility = visibility + 50

                 fog = code in fogCodes
                 thunder = code in thunderCodes
                 ice = code in iceCodes

                 dic = {'date': hour['time'][0:10], 'hour': hour['time'][11:16], 'windspeed': windspeed, 'visibility': visibility, 'fog': fog, 'rain': hour['will_it_rain'],
                        'snow': hour['will_it_snow'], 'thunder': thunder, 'ice': ice}

                 dictionaries.append(dic)









        print(dictionaries)