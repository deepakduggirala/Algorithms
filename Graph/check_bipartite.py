# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:44:21 2015

@author: Deepak
"""



from graph import unDGraph
import Queue


def check_bipartite(g,start = 0):
    N = len(g.adjLst)
    color = [-1 for i in xrange(N)]
    queue = Queue.Queue()
    color[start] = 1
    queue.put(start)
    
    while not queue.empty():
        u = queue.get()
        for v in g.adjLst[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
            elif color[v] == color[u]:
                return False
    return True

N = 4
g = unDGraph(N)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(2,3)

print check_bipartite(g,0)
                    
                
    
