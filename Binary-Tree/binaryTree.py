# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:07:10 2015

@author: deep
"""
import random
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
