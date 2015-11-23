# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:26:01 2015

@author: Deepak
"""

from graph import unDGraph

def greedyColoring(g):
    N = len(g.adjLst)
    color = [-1 for i in xrange(N)]
    color[0] = 0
    
    availableClrs = [True for i in xrange(N)]
    for u in xrange(1,N):
        for v in g.adjLst[u]:
            #Process all adjacent vertices and flag their colors as unavailable
            if color[v] != -1:
                availableClrs[color[v]] = False
        cr = availableClrs.index(True)
        color[u] = cr
        availableClrs = [True for i in range(N)]
    for u in xrange(N):
        print u,color[u]

g1 = unDGraph(5)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(1, 3)
g1.addEdge(2, 3)
g1.addEdge(3, 4)

greedyColoring(g1)

g2 = unDGraph(5)

g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(1, 2)
g2.addEdge(1, 4)
g2.addEdge(2, 4)
g2.addEdge(4, 3)
print ''
greedyColoring(g2)
