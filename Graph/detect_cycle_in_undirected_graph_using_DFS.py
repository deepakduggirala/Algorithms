# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:03:43 2015

@author: deep
"""

from graph import unDGraph

def detectCycleUnDgraph(g):
    stack = []
    N = len(g.adjLst)
    visited = [False for i in range(N)]
    
    u = 0
    visited[u] = True
    stack.append((u,None))
    while stack:
        #print stack
        x,parent = stack.pop()
        i = 0
        for vertex in g.adjLst[x]:
            #print 'visiting',vertex,'from',x
            if not visited[vertex]:
                visited[vertex] = True
                #print 'setting',vertex,'as visited'
                stack.append((vertex,x))
                i = i+1
            else:   #trying to reach a vertex that has already been visited
                if vertex != parent: #if this vertex is something else than the parent vertex
                    return True
    #print visited
    return False
    
    
N = 6
g = unDGraph(N)
g.addEdge(0,5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)
#print g.adjLst
print detectCycleUnDgraph(g)
