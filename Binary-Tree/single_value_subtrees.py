# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:13:58 2015

@author: deep
"""

from binaryTree import BTree, generateRandomTree

def SVSubTrees(root):
    count1,count2,st1,st2 = 0,0,True,True
    if root.left:
        count1,st1 = SVSubTrees(root.left)
    if root.right:
        count2,st2 = SVSubTrees(root.right)
    if root.left is None and root.right is None:
        return 1,True
    if root.left and root.right:
        if root.value == root.left.value and root.value == root.right.value:
            if st1 is True and st2 is True:
                st = True
                count = count1+count2 + 1
            else:
                count = count1+count2
                st = False
        else:
            count = count1+count2
            st = False
    else:
        if root.left:
            if root.value == root.left.value:
                count  = count1+1
                st = True
            else:
                count = count1
                st = False
        else:
            if root.value == root.right.value:
                count  = count1+1
                st = True
            else:
                count = count1
                st = False
    return count,st
        
    
root1 = BTree()
root1.value = 0
generateRandomTree(root1,2)
print SVSubTrees(root1)
