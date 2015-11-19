# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:11:33 2015

@author: deep
"""
from binaryTree import BTree, generateRandomTree, inorder

def mirror(root):
    if root:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left
        
    
root1 = BTree()
root1.value = 0
generateRandomTree(root1,2)
mirror(root1)
inorder(root1)
