
#Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
# 
#
#Example 1:
#
#
#Input: root = [3,1,4,null,2], k = 1
#Output: 1
#Example 2:
#
#
#Input: root = [5,3,6,2,4,null,null,1], k = 3
#Output: 3
# 
#
#Constraints:
#
#The number of nodes in the tree is n.
#1 <= k <= n <= 104
#0 <= Node.val <= 104
# 
#
#Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root,myList):
        if not root:
            return
        if root.left:
            self.DFS(root.left,myList)
        
        myList.append(root.val)
        
        if root.right:
            self.DFS(root.right,myList)
        return
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # you can probably put this into a heap and then pop off the heap like 
        # in python you can also do the same thing in a list
        # you just DFS into the tree put the values into a list and sort it
        
        
        myList = []
        
        self.DFS(root, myList)
        
        return myList[k - 1]
        