# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeToArray(self,root,array):
        if not root:
            return
        self.treeToArray(root.left,array)
        array.append(root.val)
        self.treeToArray(root.right,array)
        return
    
        
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # so we essentially wanna see if subroot exists exactly within root
        # that means leaves and roots match up
        # no extra leaves, also all node values must match
        # im thinking output subroot to and array, output root to an array and see if subroot array exists within root array
        # ok so outputting to array is not a solution, i wanted to make it fast but looks like you can't really
        # instead, just to DFS and if you find subroot.value, then DFS compare all children
        # ok so here we should first fine the subroot value, if not there then its false
        # if we find it then we do a tree compare
        # lets do BFS to traverse and search for my value
        # oh values are not unique so we ned to check all instances
        
        subRootArray = []
        self.treeToArray(subRoot,subRootArray)
        
        queue = [root]
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node.val == subRoot.val:
                rootArray = []
                self.treeToArray(node,rootArray)
                if rootArray == subRootArray:
                    return True
                
        return False
        
        
        