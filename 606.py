# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root):
        # first base case
        if not root:
            return ""
        if root.left and not root.right:
            return str(root.val) + '(' + self.DFS(root.left) + ')'
        if not root.left and root.right:
            return str(root.val) + '()' + '(' + self.DFS(root.right) + ')'
        if not root.left and not root.right:
            return str(root.val)
        
        return str(root.val) + '(' + self.DFS(root.left) + ')' + '(' + self.DFS(root.right) + ')'
        
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # so we need it to output preorder traversal
        # but also there are some caveats
        # for any node four things can happen
        # there (not l and not r) (not l and r) (l and not r) (l and r)
        # these all are slightly different and may need to be treated differently
        
        return self.DFS(root)