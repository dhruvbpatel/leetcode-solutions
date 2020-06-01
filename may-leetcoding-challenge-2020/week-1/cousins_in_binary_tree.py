# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,root,x,y,parent,lev,xlist,ylist):
        if root is None:
            return False
        if root.val == x:
            xlist.append((lev,parent))
        if root.val==y:
            ylist.append((lev,parent))
        
        self.dfs(root.left,x,y,root,lev+1,xlist,ylist)
        self.dfs(root.right,x,y,root,lev+1,xlist,ylist)
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = None
        xlist=[]
        ylist=[]
        lev=0
        
        self.dfs(root,x,y,parent,lev,xlist,ylist)
        
        return xlist[0][0]==ylist[0][0] and xlist[0][1]!=ylist[0][1]
    
    
        
        
        