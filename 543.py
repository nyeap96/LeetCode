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
        leftDepth = self.DFS(root.left)
        rightDepth = self.DFS(root.right)
        self.currentBest = max(self.currentBest,leftDepth + rightDepth)
        
        return max(leftDepth,rightDepth) + 1
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ok so this one seems to almost be like a height problem
        # so we can gaurantee one thing which is that one of the nodes in question will be the deepest node
        # the qustion really becomes how can i tell what the other farthest node is
        # it can be anywhere in theory, it doesnt have to be on the other side of the root
        # i think what we need to compare the following three values
        # depth of left + depth of right vs depth of child + current depth + depth of other side of root
        # we need a global to keep track of the best values since we need to go bottom up
        # so usually i try to go top down, but that didnt work out too well here, and instead i need to do a bottom up approach
        #
        self.currentBest = 0
        self.DFS(root)
        return self.currentBest
        
        