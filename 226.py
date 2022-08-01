# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root):
        if not root:
            return
        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
        elif root.left and not root.right:
            root.right = root.left
            root.left = None
        elif not root.left and root.right:
            root.left = root.right
            root.right = None
        self.DFS(root.left)
        self.DFS(root.right)
        return
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # so inverting a tree is essentially reversing the values on each level of the tree
        # So this means that you need to read all values on each level before rewriting your tree
        # so the easiest way will probably be to either read all values or do a BFS
        # This makes me want to do the following
        # first do left sided DFS and record each value inorder
        # althought it doesnt really matter technically cause i could just sort the values afterwards
        # also i can already see an isue if the tree is not balanced
        # if the tree is not symmetrical(rather than balanced) then you would have to make the odd node parent someone else
        # ok so the tree does not have to be symmetrical so rather than DFS i want to do BFS i think 
        # i think the only way i know how to do BFS is using the stack method
        # okay so the BFS method is possible but idk what it is atm
        # but this problem sjohulndt require it
        # it looks like the best way is to simply invert every subtree is the answer
        # so for every treenode you simply make root.left = root.right and root.right = root.left
        
        self.DFS(root)
        return root
        
        
        
        
        