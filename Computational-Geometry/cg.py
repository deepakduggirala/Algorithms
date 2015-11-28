# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:44:17 2015

@author: deepak
"""

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)

def cross(p1,p2):
    return p1.x*p2.y - p2.x*p1.y

def direction(p1,p2,p3):
    return cross(p3-p1, p2-p1)

def segmentsIntersect(p1,p2,p3,p4):
    #quick rejection
    x1h = min(p1.x, p2.x)
    y1h = min(p1.y, p2.y)
    
    x2h = max(p1.x, p2.x)
    y2h = max(p1.y, p2.y)
    
    x3h = min(p3.x, p4.x)
    y3h = min(p3.y, p4.y)
    
    x4h = max(p3.x, p4.x)
    y4h = max(p3.y, p4.y)
    
    if not x2h >= x3h and x4h >= x1h and y2h >= y3h and y4h >= y1h:
        return False
    #Check if one straddles the other
    
    d1 = direction(p1,p2,p3)
    d2 = direction(p1,p2,p4)
    
    if (d1 < 0 and d2 > 0) or (d1 > 0 and d2 < 0):
        return True
    #p3 or p4 lies on p1p2
    if d1 == 0 or d2 == 0:
        return True
