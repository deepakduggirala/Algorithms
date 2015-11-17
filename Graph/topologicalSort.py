# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:33:04 2015

@author: deep
"""
from graph import Graph

#Assumes vertices are numbered from zero to N-1
def topologicalSort(g):
    N = len(g.adjLst)
    indegree = [0 for i in range(N)]
    for u,vLst in enumerate(g.adjLst):
        for v in vLst:
            indegree[v] = indegree[v]+1
    sortedVertices = []
    #add all vertices with indegree 0 to the stack
    stack = [i for i in range(N) if indegree[i]==0]
    while stack:
        u = stack.pop()
        sortedVertices.append(u)
        for v in g.adjLst[u]:
            indegree[v] = indegree[v]-1
            if indegree[v] == 0:
                stack.append(v)
    if len(sortedVertices) == N:
        return sortedVertices
    print 'Contains Cycle'
    return False

N = 6
g = Graph(N)
g.addEdge(0,5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
#g.addEdge(4,1)
#g.addEdge(5,0)
print topologicalSort(g)
