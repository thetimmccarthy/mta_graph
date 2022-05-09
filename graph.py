import pandas as pd
from station import Station
import heapq
from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.edges = self.buildEdges(directed)
        


    def buildEdges(self, directed):
    
        # pre-built CSV of edges - made up of 
        # actual edges (i.e. two connected stops) and transfer
        edgesDF = pd.read_csv('./data/edges.csv')

        edges = {}

        for index, row in edgesDF.iterrows():
            x = row['from'] 
            y = row['to']
            w = row['weight']

            fromName = Station.getStationByName(x) 
            toName = Station.getStationByName(x)
        
            self.insertEdge(edges, x,y,w, fromName, toName, directed)
        
        return edges

    def insertEdge(self, edges, startStation, endStation, weight, fromName, toName, directed):
        end = Station()
        end.stationID = endStation
        end.weight = weight
        end.stationName = toName
        
        # if starting station already in edge list, append to front of linkedlist
        if startStation in edges:
            temp = edges[startStation]
            end.nextStation = temp
            edges[startStation] = end
        # else, add to edge list
        else:
            edges[startStation] = end
        
        if not directed:
            self.insertEdge(edges, endStation, startStation, weight, toName, fromName, True)
        
        return
    ## Dijkstra's Shortest Path algorithm
    ## takes a starting station and finds shortest path to all stations
    def findShortestPath(self, startPoint):
        shortestPath = defaultdict(lambda: float('inf'))
        shortestPath[startPoint] = 0

        parent = defaultdict(str)

        q = []
        heapq.heappush(q, (0, startPoint))
        while len(q) != 0:
            curr = heapq.heappop(q)
            while curr[0] > shortestPath[curr[1]]:
                curr = heapq.heappop(q)
            
            curr = curr[1]
            currEdge = self.edges[curr]
            while currEdge:
                dist = shortestPath[curr] + currEdge.weight
                if dist < shortestPath[currEdge.stationID]:
                    shortestPath[currEdge.stationID] = dist
                    parent[currEdge.stationID] = curr
                    heapq.heappush(q, (shortestPath[currEdge.stationID], currEdge.stationID))
                
                currEdge = currEdge.nextStation
        return shortestPath, parent


    def previousStop(self, parent, end):
        return parent[end]
    
    def getPath(self, parentDict, start, end):
        if start == end:
            return []
        path = [end]
        nextStop = self.previousStop(parentDict, end)
        while nextStop != start:
            path.append(nextStop)
            nextStop = self.previousStop(parentDict, nextStop)
        
        path.append(nextStop)
        return path[::-1]



        
    
    