# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,currentPath,paths):
        if not root:
            return
        
        currentPath.append(root.val)
        if root.left != None:
            self.DFS(root.left,currentPath,paths)
        if root.right != None:
            self.DFS(root.right,currentPath,paths)
        if root.left == None and root.right == None:
            pathStr = ""
            for nodeVal in currentPath:
                pathStr += str(nodeVal) + "->"
            paths.append(pathStr[:-2])
        currentPath.pop()
        return
        
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        currentPath = []
        paths = []
        
        self.DFS(root,currentPath,paths)
        return paths
        