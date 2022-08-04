"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def DFS(self,root,listArray):
        if not root:
            return
        listArray.append(root.val)
        for child in root.children:
            self.DFS(child,listArray)
        return
    
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.DFS(root,res)
        return res