# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        
#         if root.val == val:
#             return root
        
        if root.val>val:
            root=self.searchBST(root.left,val)
        elif root.val<val:
            root=self.searchBST(root.right,val)
        
        return root
        
        
            
        
        