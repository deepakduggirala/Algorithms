# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:35:13 2015

@author: deep
"""

from binaryTree import BTree, generateRandomTree, inorder
import Queue

def levelOrderReverse(root):
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        x = q.get()
        print x.value
        if x.right is not None:
            q.put(x.right)
        if x.left is not None:
            q.put(x.left)
        

root1 = BTree()
root1.value = 0
generateRandomTree(root1,2)
inorder(root1)
print ''
levelOrderReverse(root1)
