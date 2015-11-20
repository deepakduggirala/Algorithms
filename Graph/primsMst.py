# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:56:15 2015

@author: Deepak
"""

from graph import weightedUnDGraph
import heapq

def PrimsMST(g,start = None):
    N = len(g.adjLst)
    Edges = [[w,u,v] for u,wvList in enumerate(g.adjLst) for w,v in wvList]
    if start is None:
        minEdge = min(Edges)
        start = minEdge[1]
    
    visited = [False for i in xrange(N)]
    mstEdges = []
    parent = start
    heap = [(0,start, None)]
    heapq.heapify(heap)
    cost = 0
    while heap:
        dist, u, parent = heapq.heappop(heap)
        if not visited[u]:
            visited[u] = True
            mstEdges.append((parent, u))
            cost = cost + dist
            for w,v in g.adjLst[u]:
                if not visited[v]:
                    heapq.heappush(heap, (w,v,u))
            parent = u
    return mstEdges[1:],cost
    
N = 9
g = weightedUnDGraph(N)
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,2,8)
g.addEdge(2,3,7)
g.addEdge(3,4,9)
g.addEdge(4,5,10)
g.addEdge(5,6,2)
g.addEdge(6,7,1)
g.addEdge(7,0,8)
g.addEdge(1,7,11)
g.addEdge(7,8,7)
g.addEdge(2,8,2)
g.addEdge(8,6,6)
g.addEdge(2,5,4)
g.addEdge(3,5,14)

print PrimsMST(g)
