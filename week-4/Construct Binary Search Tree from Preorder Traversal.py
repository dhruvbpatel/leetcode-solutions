# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        if not preorder:  ## our base case
            return None 
        
        rootNode = TreeNode(preorder[0])  ## crete a root node
        
        i=1
        j = len(preorder)
        
        
        while i<j:
            if preorder[0]>preorder[i]:  ## find the 1st val in preorder where element is bigger than rootval
                i+=1   ## make index till there
            else:
                break ## 1st big element found, break
        
        ## apply recursion simply 
        rootNode.left = self.bstFromPreorder(preorder[1:i])  ## now till our i , is all left side elements
        rootNode.right = self.bstFromPreorder(preorder[i:])  ## an from i to end is all our right side ele
        
        return rootNode 
        
        
        
        
            
            
            
            
        
        