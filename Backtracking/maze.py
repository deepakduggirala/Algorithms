# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:35:59 2015

@author: Deepak
"""
import time
def outside(x,y):
    if x >= len(maze) or y >= len(maze[0]):
        return True
    if x < 0 or y < 0:
        return True
    return False

def find_path(x,y):
    global path
    print x,y
    if outside(x,y):
        return False
    if (x,y) == goal:
        return True
    if maze[x][y] != 1:
        return False
    maze[x][y] = '+'
    path.append((x,y))
    if find_path(x-1,y):    #North
        return True
    if find_path(x,y+1):    #East
        return True
    if find_path(x+1,y):    #South
        return True
    if find_path(x,y-1):    #West
        return True
    maze[x][y] = 1
    path.pop()
    return False
    
maze = [[1,0,0,0],
        [1,1,0,1],
        [0,1,0,0],
        [1,1,1,1]]
path = []
goal = (3,3)
print find_path(0,0)
print path
