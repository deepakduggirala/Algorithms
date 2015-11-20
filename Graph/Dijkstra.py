# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:41:46 2015

@author: deep
"""
from graph import weightedGraph
import heapq
def djikstra(a,S):
    N = len(a.adjLst)
    Visited = [False for i in xrange(N)]
    Distance = [float('inf') for i in xrange(N)]
    Distance[S] = 0
    heap = []
    heapq.heappush(heap,(0,S))
    for i in xrange(N):
        if heap:
            while(True):
                _,u = heapq.heappop(heap)
                if not Visited[u]:
                    break
            Visited[u] = True
            for weight_uv,v in a.adjLst[u]:
                if not Visited[v]:
                    if Distance[v] > Distance[u] + weight_uv:
                        Distance[v] = Distance[u] + weight_uv
                        heapq.heappush(heap, (Distance[v],v))
    print Distance
    return Distance
    
g = weightedGraph(4)
g.addEdge(0,1,1)
g.addEdge(1,2,2)
g.addEdge(2,3,3)
g.addEdge(3,0,4)
djikstra(g,0)
