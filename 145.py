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
        if root.right:
            self.DFS(root.right,myList)
        
        myList.append(root.val)
        return
        
        
        
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case (root is nothing) in that case you return empty list
        
        # after this is a relatively proper tree
        # keep a global variable to hold result or return result
        # 
        # 
        if not root:
            return []
        
        myList = []
        self.DFS(root,myList)
        return myList
        
        
        
        
        
        