# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:52:16 2015

@author: Deepak
"""

def knapsack01(wts, val, totalWt):
    matrix = [[0 for j in xrange(totalWt+1)] for i in xrange(len(wts)+1)]
    includedWts = []
    for i in range(1,len(wts)+1):
        for t in range(1,totalWt+1):
            wt = wts[i-1]
            if t >= wt:
                matrix[i][t] = max(matrix[i-1][t-wt]+val[i-1], matrix[i-1][t])
            else:
                matrix[i][t] = matrix[i-1][t]
       
    i = len(wts)
    j = totalWt
    while i>=1 and j>=1:
        if matrix[i][j] != matrix[i-1][j]:
            includedWts.append(wts[i-1])
            j = j-wts[i-1]
        i = i-1
    return matrix[-1][-1], includedWts
wts = [1,3,4,5]
val = [1,4,5,7]
totalWt = 7

print knapsack01(wts, val, totalWt)
