# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:41:42 2015

@author: deep
"""
from graph import Graph
import Queue

def BFS(g, u):
    N = len(g.adjLst)
    visited = [False for i in range(N)]
    q = Queue.Queue()
    visited[u] = True
    q.put(u)    
    while not q.empty():
        x = q.get()
        for vertex in g.adjLst[x]:
            if not visited[vertex]:
                visited[vertex] = True               
                q.put(vertex)



N = 4
g = Graph(N)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

BFS(g, 0)
