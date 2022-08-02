"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def DFS(self,root):
        depths = []
        for child in root.children:
            depths.append(self.DFS(child))
        if not depths:
            return 1
        else:
            return max(depths) + 1
        
    
    def maxDepth(self, root: 'Node') -> int:
        # here we wanna do bottom up depth calculation
        # so do DFS and return depth or something we wanna get the max depth from all children not just left and right though
        if not root:
            return 0
        return self.DFS(root)
        