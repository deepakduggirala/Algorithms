# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:51:59 2015

@author: Deepak
"""

class subset():
    def __init__(self,p,r):
        self.parent = p
        self.rank = r

class disjointSet():
    def __init__(self,data):
        N = len(data)
        self.subsets = [0 for x in xrange(N)]
        for x in data:
            self.subsets[x] = subset(x,0)
    def find(self,x):
        if self.subsets[x].parent != x:
            self.subsets[x].parent = self.find(self.subsets[x].parent)
        return self.subsets[x].parent
    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        a = self.subsets[x_root].rank
        b = self.subsets[y_root].rank
        min_root, max_root = (x_root,y_root) if a<b else (y_root,x_root)
        self.subsets[min_root].parent = max_root
        if a == b:
            self.subsets[max_root].rank = self.subsets[max_root].rank + 1
        
a = range(7)
dSet = disjointSet(a)
print dSet.find(1)
dSet.union(0,1)
dSet.union(3,4)
print dSet.find(1)
