# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self,root,currentPath,target):
        if not root:
            return
        
        currentPath.append(root)
        if root.val == target:
            return
        elif root.val > target:
            self.DFS(root.left,currentPath,target)
        elif root.val < target:
            self.DFS(root.right,currentPath,target)
        return
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentPath = []
        pathP = []
        pathQ = []
        self.DFS(root,currentPath,p.val)
        pathP = currentPath
        
        currentPath = []
        self.DFS(root,currentPath,q.val)
        pathQ = currentPath
        
        if len(pathQ) >= len(pathP):
            smallerPath = pathP
        else:
            smallerPath = pathQ
        
        for i in range(0,len(smallerPath)):
            if pathP[i].val != pathQ[i].val:
                return pathP[i - 1]
        return smallerPath[len(smallerPath) - 1]
        
         
         
        
        
        