# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:08:55 2015

@author: deep
"""

def evalPostfix(expr):
    operators = ['+','-','*','/']
    operands_stack = []
    for x in expr:
        if x not in operators:
            operands_stack.append(x)
        else:
            left = operands_stack.pop()
            right = operands_stack.pop()
            result = str(eval(left+x+right))
            operands_stack.append(result)
    return operands_stack.pop()

print evalPostfix('231*+9-')
