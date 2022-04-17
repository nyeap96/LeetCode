#Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
#
# 
#
#Example 1:
#
#
#Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
#Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#Example 2:
#
#
#Input: root = [5,1,7]
#Output: [1,null,5,null,7]
# 
#
#Constraints:
#
#The number of nodes in the given tree will be in the range [1, 100].
#0 <= Node.val <= 1000



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def DFS(root):
            if root:
                DFS(root.left)
                root.left = None
                self.resultTree.right = root
                self.resultTree = root
                DFS(root.right)
        
        
        # this one seems like a sort of DFS problem
        # you want to rearrange the tree from smallest to largest.
        # i think the plan is to recurse down all the way left
        # at first i tried to rearrange the array without any extra memory, but the better idea here is to just have dummyNode and then use the dummynode to point to what i want
        
        dummy = TreeNode(0)
        self.resultTree = dummy
        DFS(root)
        return dummy.right
        
        
        