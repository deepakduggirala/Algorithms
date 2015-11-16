# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:24:31 2015

@author: deep
"""

import random
import Queue

class BTree():
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        
def generateRandomTree(root, height):
    parent = root
    if height > 0:
        leftNode = BTree()
        leftNode.value = random.randint(1,100)
        parent.left = leftNode
        
        rightNode = BTree()
        rightNode.value = random.randint(1,100)
        parent.right = rightNode
        
        generateRandomTree(leftNode, height-1)
        generateRandomTree(rightNode, height-1)

def inorder(root):
    if root:
        inorder(root.left)
        print root.value,
        inorder(root.right)

def preorder(root):
    if root:
        print root.value,
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.value,

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

def mirror(root):
    if root:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left
        
def root_to_leaf(root):
    arr = []
    if root.left is None and root.right is None:
        return [[root.value]]
    for s in root_to_leaf(root.left):
        s.append(root.value)
        arr.append(s)
    for s in root_to_leaf(root.right):
        s.append(root.value)
        arr.append(s)
    return arr
def root_to_leaf_cover(root):
    for s in root_to_leaf(root1):
        s.reverse()
        for n in s:
            print n,
        print ''

#count of single valued subtreses
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
                
def maxPathSum(root):
    pass
    
def levelOrder(root):
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        x = q.get()
        print x.value
        if x.left is not None:
            q.put(x.left)
        if x.right is not None:
            q.put(x.right)
            
def levelOrderTraversalReverse():
    pass
def levelOrderTraversalSpiral():
    pass
        



root1 = BTree()
root1.value = 0
generateRandomTree(root1,2)
inorder(root1)

print ''
print levelOrder(root1)


