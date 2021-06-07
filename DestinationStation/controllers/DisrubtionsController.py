import datetime
import json
import sys
sys.path.insert(1, '../services/')

import DestinationStation.services.NSDisrubtionsAPI as NSDisrubtionsAPI

class DisrubtionsController:

    def getDisrubtions(time, stationCode):
        data = NSDisrubtionsAPI.NSDisrubtionsAPI.getDisrubtion(stationCode)
        if data != []:
            if data['type'] == "MAINTENANCE":
                if datetime.data['end'] > datetime.time > datetime.data['start']:
                    return True
        else:
            return 'kur'