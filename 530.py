# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root,valList):
        if not root:
            return
        if root.left:
            self.DFS(root.left,valList)
        valList.append(root.val)
        if root.right:
            self.DFS(root.right,valList)
        return
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # here we can do DFS and then simply compare root to its children
        # this is allowed because its a BST meaning that for any node the numbers closest to it are its parent and its children
        # so we simply look fo rth parnet/child pair that are closest in value and return that value
        # so the way it should work is the following
        # we'll do DFS then when we hit the leftmost node we return cause no children
        # then we go down the right side  and return the minimum value from there
        # so we want to resolve both the left and right sides before clcaulting our own children differences
        # so we need to save the min values from both left and right
        # then we compare the smaller value to 
        
        # ok so i misunderstood the problem again
        # so here we just need to find the two closest values is all that we need to do
        # so what we do is store all the values and then 
        
        # okay so since its a bst and i did DFS, then the values are sorted so we only need to compare all value next to each other cause they are closest in value so the answer must be in there somwhere
        valList = []
        self.DFS(root,valList)
        
        minDiff = 100000
        for i in range(1,len(valList)):
            minDiff = min(minDiff, abs(valList[i] - valList[i -1]))
        return minDiff
        
        
        
        
        