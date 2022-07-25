# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root,isLeft,res):
        if not root:
            return res
        
        if root.left:
            res = self.DFS(root.left,True,res)
        if root.right:
            res = self.DFS(root.right,False,res)
        
        if isLeft:
            if root.left == None and root.right == None:
                res += root.val
        return res
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # this seems like a problem that can be solved using DFS again
        # however, the question becomes how can ou identify a left leaf
        # a left leaf is a node that is a leaf, which is a node that had no children
        # and a node that is a left child of another node
        # this should be achieveable by simply adding another parameter to the DFS function that tells the function whether or not the node is a left node
        
        res = 0
        res = self.DFS(root,False,res)
        return res
        