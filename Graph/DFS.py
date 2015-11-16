# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 21:21:55 2015

@author: deep
"""

from graph import Graph

def DFS(g, u):
    stack = []
    N = len(g.adjLst)
    visited = [False for i in range(N)]
    pre = [0 for i in range(N)]
    post = [0 for i in range(N)]
    count  = 1
    
    visited[u] = True
    pre[u] = count
    count = count + 1
    stack.append(u)
    while stack:
        x = stack[-1]
        i = 0
        for vertex in g.adjLst[x]:
            if not visited[vertex]:
                visited[vertex] = True
                stack.append(vertex)
                pre[vertex] = count
                count = count + 1
                i = i+1
        if i == 0:  #deadend
            stack.pop()
            post[x] = count
            count = count + 1
    #print visited
    return pre,post

def detectBackEdges(g, pre, post):
    edges = []
    for u,vLst in enumerate(g.adjLst):
        for v in vLst:
            edges.append((u,v))
    backEdges = []
    for u,v in edges:
        if pre[v] <= pre[u] <= post[u] <= post[v]:
            backEdges.append((u,v))
        #print u,v,pre[u],post[u],pre[v],post[v]
    return backEdges
    
N = 2
g = Graph(N)
g.addEdge(0, 1)
g.addEdge(1, 0)


pre, post = DFS(g, 0)
print detectBackEdges(g,pre,post)
