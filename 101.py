# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,left,right):
        
        if not left and not right:
            #print("not left and not right")
            return True
        #elif (left and not right) or (not left and right) or (left.val != right.val):
        elif (left and not right):
            #print("left and not right")
            return False
        
        elif (not left and right):
            #print("not left and right")
            return False
        
        elif (left.val != right.val):
            #print("values not equal")
            return False
        
        return self.DFS(left.left, right.right) and self.DFS(left.right, right.left)
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.DFS(root.left,root.right)
        
        
        
        
        