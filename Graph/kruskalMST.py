# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:38:54 2015

@author: Deepak
"""

from graph import weightedUnDGraph
from disjointSet import disjointSet

def cmpr(x,y):
    if x[2] != y[2]:
        return cmp(x[2],y[2])
    a = x[0]+x[1]+x[2]
    b = y[0]+y[1]+y[2]
    if a < b:
        return -1
    if a == b:
        return 0
    return 1

def kruskalsMST(g,start=None):
    N = len(g.adjLst)
    Edges = [[u,v,w]for u, wvList in enumerate(g.adjLst) for w,v in wvList]
    Edges.sort(cmp = cmpr)    
    TV = disjointSet(range(N))
    TE = []
    cost, numEdges, i = 0,0,0
    while numEdges < N and i < len(Edges):
        u,v,wt = Edges[i]
        if TV.find(u) != TV.find(v):
            TV.union(u,v)
            TE.append([u,v])
            cost = cost + wt
            numEdges = numEdges + 1
        i = i+1
    return cost,TE
    
    
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

print kruskalsMST(g)
