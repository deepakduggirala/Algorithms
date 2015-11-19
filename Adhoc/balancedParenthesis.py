# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:22:56 2015

@author: deep
"""

def balancedParenthesis(expr):
    openBrackets = ['(','[','{']
    closedBrackets = [')',']','}']
    stack = []
    for x in expr:
        if x in openBrackets:
            stack.append(x)
        elif x in closedBrackets:
            y = stack.pop()
            yi = openBrackets.index(y)
            xi = closedBrackets.index(x)
            if xi != yi:
                return False
    if len(stack):
        return False
    return True

print balancedParenthesis('(1+(2+3))')
