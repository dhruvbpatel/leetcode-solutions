# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder_tree=[]
    
    def getList(self,root,k):
        if(root is None):
            return
        
        self.getList(root.left,k)
        self.inorder_tree.append(root.val)
        self.getList(root.right,k)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.getList(root,k)
        print(self.inorder_tree)
        ans = self.inorder_tree[k-1]
        return ans
        
        
        
        
        
        