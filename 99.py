#You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
#
# 
#
#Example 1:
#
#
#Input: root = [1,3,null,null,2]
#Output: [3,1,null,null,2]
#Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
#Example 2:
#
#
#Input: root = [3,1,4,null,null,2]
#Output: [2,1,4,null,null,3]
#Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [2, 1000].
#-231 <= Node.val <= 231 - 1





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
    
    def replace(self,root,valOne,valTwo):
        if not root:
            return
        
        if root.left:
            self.replace(root.left,valOne,valTwo)
        
        if root.val == valOne:
            root.val = valTwo
        elif root.val == valTwo:
            root.val = valOne

        if root.right:
            self.replace(root.right,valOne,valTwo)
            
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # here i think you should do a DFS algorithm
        # when you do DFS on a binary search tree, normally it should print in ascending order
        # if it doesnt thats where you know the value is messed up
        
        myList =[]
        self.DFS(root,myList)
        
        toSwitchOne = 0
        
        for i in range(1,len(myList)):
            if myList[i] < myList[i - 1]:
                toSwitchOne = i - 1
                break
        toSwitchOne = myList[toSwitchOne]
        
        toSwitchTwo = 0
        for i in range(len(myList) - 1,-1,-1):
            if myList[i] < toSwitchOne:
                toSwitchTwo = myList[i]
                break
        
        self.replace(root,toSwitchOne,toSwitchTwo)
        
        
        
                
        