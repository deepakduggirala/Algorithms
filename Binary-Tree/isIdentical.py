# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:06:16 2015

@author: deep
"""
from binaryTree import BTree, generateRandomTree
def isIdentical(root1, root2):
    if  root1 is None and root2:
        return False
    if root1 and root2 is None:
        return False
    if root1 is None and root2 is None:
        return True
    if root1.value == root2.value:
        return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
    return False
    
root1 = BTree()
root1.value = 0
generateRandomTree(root1,2)
print isIdentical(root1, root1)
