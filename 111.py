# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root,depth,leaves):
        if not root:
            return
        if root.left:
            self.DFS(root.left,depth + 1,leaves)
        if root.right:
            self.DFS(root.right,depth + 1,leaves)
        if not root.left and not root.right:
            leaves.append(depth)
        
        return
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leaves = []
        self.DFS(root,1,leaves)
        print(leaves)
        return min(leaves)