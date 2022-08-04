"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def DFS(self,root,arrayList):
        if not root:
            return
        for child in root.children:
            self.DFS(child,arrayList)
        arrayList.append(root.val)
        return
    
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.DFS(root,res)
        return res