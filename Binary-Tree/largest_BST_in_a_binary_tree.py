# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:38:50 2015

@author: deep
"""

from binaryTree import BTree, generateRandomTree, inorder

def largestBST(root):
    if root.left is None and root.right is None:
        return True, 1, root.value, root.value
    if root.left:
        isBSTL, sizeL, minL, maxL = largestBST(root.left)
    else:
        isBSTL = True
        sizeL = 0
        minL = -float('inf')
    if root.right:
        isBSTR, sizeR, minR, maxR = largestBST(root.right)
    else:
        isBSTR = True
        sizeR = 0
        maxR = float('inf')
    if isBSTL and isBSTR:
        if maxL <= root.value <= minR:
            return True, sizeL+sizeR+1, minL, maxR, 
    size = max(sizeL, sizeR)
    return False, size , None, None
        

root1 = BTree()
root1.value = 0
root2 = BTree()
root2.value = 0
generateRandomTree(root2,2)
generateRandomTree(root1,2)
root1.left.left.left = root2
inorder(root1)
print largestBST(root1)
