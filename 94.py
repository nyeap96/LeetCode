# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,result):
        if not root:
            return
        
        if root.left:
            self.DFS(root.left,result)
        result.append(root.val)        
        if root.right:
            self.DFS(root.right,result)
        return
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        self.DFS(root,result)
        return result