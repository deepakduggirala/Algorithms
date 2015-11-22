# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:33:04 2015

@author: deep
"""
from graph import weightedGraph

#Assumes vertices are numbered from zero to N-1
def topologicalSort(g):
    N = len(g.adjLst)
    indegree = [0 for i in range(N)]
    LPT = [0 for i in range(N)]
    for u,vLst in enumerate(g.adjLst):
        for w,v in vLst:
            indegree[v] = indegree[v]+1
    sortedVertices = []
    #add all vertices with indegree 0 to the stack
    stack = [i for i in range(N) if indegree[i]==0]
    while stack:
        u = stack.pop()
        sortedVertices.append(u)
        for w,v in g.adjLst[u]:
            indegree[v] = indegree[v]-1
            LPT[v] = max(LPT[v], LPT[u]+w)
            if indegree[v] == 0:
                stack.append(v)
    if len(sortedVertices) == N:
        return sortedVertices, LPT
    print 'Contains Cycle'
    return False

N = 6
g = weightedGraph(N)
g.addEdge(0,2,3)
g.addEdge(0,1,5)
g.addEdge(1,3,6)
g.addEdge(2,3,7)
g.addEdge(2,5,2)
g.addEdge(3,4,-1)
g.addEdge(3,5,1)
g.addEdge(2,4,4)
g.addEdge(4,5,-2)
print topologicalSort(g)
