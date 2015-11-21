# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:31:01 2015

@author: deep
"""

class Graph():
    def __init__(self,N):
        self.adjLst = [[] for i in range(N)]
    def addEdge(self,u,v):        
        self.adjLst[u].append(v)
        
class unDGraph(Graph):  #undirected graph
    def addEdge(self,u,v):
        self.adjLst[u].append(v)
        self.adjLst[v].append(u)
    
class weightedGraph(Graph):
    def addEdge(self,u,v,w):
        self.adjLst[u].append([w,v])

class weightedUnDGraph(Graph):
    def addEdge(self,u,v,w):
        self.adjLst[u].append([w,v])        
        self.adjLst[v].append([w,u])
        
class GraphM():
    def __init__(self,N):
        self.adjMat = [[None for i in xrange(N)]for i in xrange(N)]
    def addEdge(self,u,v,w=1):
        self.adjMat[u][v] = w
        
class UnDGraphM(GraphM):
    def addEdge(self,u,v,w=1):
        self.adjMat[u][v] = w
        self.adjMat[v][u] = w
