# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:43:46 2015

@author: Deepak
"""
from graph import UnDGraphM

def floyd_warshal(g):
    N = len(g.adjMat)
    W = [[[0 for k in xrange(N)]for j in xrange(N)] for i in range(2)]
    for i in xrange(N):
        for j in xrange(N):
            wt = g.adjMat[i][j]
            if wt is not None:
                W[0][i][j] = wt
            else:
                W[0][i][j] = float('inf')
    prev,now = 0,1
    for k in xrange(N):
        for i in xrange(N):
            for j in xrange(N):
                W[now][i][j] = min(W[prev][i][j], W[prev][i][k] + W[prev][k][j])
        prev, now = now, prev
    
    
    for i in range(N):
        for j in range(N):
            print '%2d'%W[prev][i][j],
        print ''
    print ''
    for i in range(N):
        for j in range(N):
            print '%2d'%W[now][i][j],
        print ''
    
    return W[prev]
    
N = 9
g = UnDGraphM(N)
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

for i in xrange(N):
    g.addEdge(i,i,0)

W = floyd_warshal(g)
