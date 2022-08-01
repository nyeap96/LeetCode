# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,valDict):
        if not root:
            return
        if root.left:
            self.DFS(root.left,valDict)
        
        if root.val in valDict:
            valDict[root.val] += 1
        else:
            valDict[root.val] = 1
        
        if root.right:
            self.DFS(root.right,valDict)
        return
    
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        # so in theory the best might be to use a heap, but i don't wanna because it's annoying to write in python so ill use a dictionary instead
        # but for the heap approach you would simply push values into the heap sorted by number of occurences. then pop from the heap as needed
        
        # ill do something similar with the dicionary.
        # ill add to the dictionary and then scan it for max number of occurences
        # then get all values that occur that many times
        
        valDict = {}
        self.DFS(root,valDict)
        print(valDict)
        
        maxOccurences = 0
        for key in valDict:
            maxOccurences = max(maxOccurences,valDict[key])
        
        res = []
        for key in valDict:
            if valDict[key] == maxOccurences:
                res.append(key)
                
        return res
        