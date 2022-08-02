# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def DFS(self,root):
        if not root:
            return 0
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        res = left + right + root.val
        root.val = abs(left - right)
        
        return res
    def addTilts(self,root):
        if not root:
            return 0
        left = self.addTilts(root.left)
        right = self.addTilts(root.right)
        return root.val + left + right
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # ok so at each node i wanna add up all the children on the right and all the children on the left
        # and then subtract and get abs value
        # ok so wat each node we need to rewrite it to be its tilt value then add all those values
        # we should seperate out those functions i think
        # so first start with tilt rewrite of maybe even tilt calculator
        self.DFS(root)
        return self.addTilts(root)
        
        