# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def DFS(self,root,myList):
        if not root:
            return
        myList.append(root.val)
        
        if root.left:
            self.DFS(root.left,myList)
        if root.right:
            self.DFS(root.right,myList)
        return
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        myList = []
        
        self.DFS(root,myList)
        return myList
    ''' 
    # solution using a stack 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        myList = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            myList.append(node.val)
            # append right first because want to visit left first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return myList
        
        
        
        
        