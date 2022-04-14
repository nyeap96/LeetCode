#You are given the root of a binary search tree (BST) and an integer val.
#
#Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
#
# 
#
#Example 1:
#
#
#Input: root = [4,2,7,1,3], val = 2
#Output: [2,1,3]
#Example 2:
#
#
#Input: root = [4,2,7,1,3], val = 5
#Output: []
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [1, 5000].
#1 <= Node.val <= 107
#root is a binary search tree.
#1 <= val <= 107





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root,val):
        if root and root.val > val:
            return self.DFS(root.left,val)
        elif root and root.val < val:
            return self.DFS(root.right,val)
        else:
            return root
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # so this is a classic DFS or BFS algorithm to do search
        # usually when i see this i prefer DFS mostly because it what i had learned to do first from my brother
        
        
        # classic DFS algorithm using recursion
        # if there is a left child, then recurse using left
        # if there is a right child recurse using right
        # return at the end
        # at first i tried to do it without helper, but its a lot easier with a help function
        
        # something i missed is that it is a binary search tree. So we don't even need actual DFS, we can throw away half the tree every single time
        # for any given node, val must be on one side or the other 
        
        
        node = TreeNode(0,None,None)
        
        node = self.DFS(root,val)
        
        return node
        