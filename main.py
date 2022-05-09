from graph import Graph
from station import Station

if __name__ == "__main__":
    g = Graph()
    start = '124'
    end = '626'

    p,j = g.findShortestPath(start)
    s = g.getPath(j, start, end)

    for i in range(len(s)):
        print(s[i], '-', Station.getStationByName(s[i]))