# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # ok so esssentially you do level traversal and then get the average
        
        res = []
        
        # so start with level traversal
        # ill use two queue to keep them seperate so i know when to stop adding and calculate average
        currentLevel = [root]
        
        while currentLevel:
            nextLevel = []
            levelSum = 0
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                levelSum += node.val
            res.append(levelSum / len(currentLevel))
            currentLevel = nextLevel
        
        return res
            
        