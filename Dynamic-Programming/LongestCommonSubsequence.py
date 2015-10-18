# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:37:37 2015

@author: deep
"""

string1 = "bisect"
string2 = "secret"

res = 0
T = [[0 for j in range(len(string2)+1)] for i in range(len(string1)+1)]
i = len(string1)-1
while i>=0:
    j = len(string2)-1
    while j>=0:
        if string1[i] == string2[j]:
            T[i][j] = T[i+1][j+1]+1
        else:
            T[i][j] = max(T[i+1][j],T[i][j+1])
        if res < T[i][j]:
            res = T[i][j]
        j = j-1
    i = i-1
print res
