# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        left = self.invertTree(root.right) ## get left most element
        right = self.invertTree(root.left) ## get right most element
        
        root.left =left
        root.right  = right
        
        
        return root
        
        