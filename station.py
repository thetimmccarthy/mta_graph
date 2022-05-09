import pandas as pd

STATIONS = pd.read_csv('./data/Stations.csv')
STATIONS['Route ID'] = STATIONS['Route ID'].astype(str)

# # List Node for edge list representation of MTA Graph
class Station:
    def __init__(self):
        self.stationID = ""
        self.weight = 0
        self.nextStation = None
        self.stationName = ""

    def getStationByName(routeID):
        try:
            x = STATIONS[STATIONS['Route ID'] == routeID]['Stop Name']
            return x.values[0]
        except IndexError:
            return routeID


