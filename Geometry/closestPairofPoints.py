# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:57:10 2015

@author: deep
"""

import random
from matplotlib import pyplot as plt
import math

def generateRandomPoints(N):
    points = []
    for i in range(N):
        points.append((random.random(), random.random()))
    return points
def plotPoints(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x,y,'ro')
    plt.show()

def scnd(x,y):
    if x[1]==y[1]:
        return 0
    elif x[1]<y[1]:
        return -1
    else:
        return 1
def distance(x,y):
    return math.sqrt((x[0]-y[0])**2, (x[1]-y[1])**2)
def closestPair(Px,Py):
    if len(Px) <= 3:
        d_AB = distance(Px[0], Px[1])
        d_BC = distance(Px[1], Px[2])
        d_CA = distance(Px[2], Px[0])
        d_min,i = min([(d_AB,0), (d_BC,1), (d_CA,2)])
        return d_min, Px[i], Px[(i+1)%3]
    Qx = Px[:len(Px)/2]
    Rx = Px[len(Px)/2:]
    Qy = []
    Ry = []
    X_Q = Qx[-1][0]
    for point in Py:
        if point[0] <= X_Q:
            Qy.append(point)
        else:
            Ry.append(point)
#    plt.hold(True)
#    x = [point[0] for point in Qy]
#    y = [point[1] for point in Qy]
#    plt.plot(x,y,'go')
#    x = [point[0] for point in Ry]
#    y = [point[1] for point in Ry]
#    plt.plot(x,y,'ro')
#    plt.hold(False)
#    plt.show()
    dQ, Q1, Q2 = closestPair(Qx, Qy)
    dR, R1, R2 = closestPair(Rx, Ry)
    d = min(dQ, dR)
    Sy = []
    for p in Qy:
        if X_Q - p[0] < d:
            pass
            

points = generateRandomPoints(25)
closestPair(points)