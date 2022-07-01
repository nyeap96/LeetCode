# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root,balanced):
        if not root:
            return 0
        left = self.DFS(root.left,balanced)
        right = self.DFS(root.right,balanced)
        
        if not abs(left - right) <= 1:
            balanced.append("false")
        
        return 1 + max(left,right)
        
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        balanced = []
        l = self.DFS(root.left,balanced)
        r = self.DFS(root.right,balanced)
        
        if balanced:
            return False
        
        if abs(l - r) <= 1:
            return True
        else:
            return False
        