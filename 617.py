# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self,root1,root2):
        if not root1 or not root2:
            return
        root1.val = root1.val + root2.val
        
        # no left root1 is missing extra left subtree so just connect it 
        if not root1.left and root2.left:
            root1.left = root2.left
            root2.left = None
        else:
            self.DFS(root1.left,root2.left)
        
        # now check for right side
        if not root1.right and root2.right:
            root1.right = root2.right
            root2.right = None
        else:
            self.DFS(root1.right,root2.right)
        return
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # so first thing to not is that both trees can be empty lets first take care of that
        if not root1 and not root2:
            return None
        if root1 and not root2:
            return root1
        elif not root1 and root2:
            return root2
        
        # ok so now we need to get the harder part
        # so merging means that all values "in the same place" are added
        # this means that for a root node, we add them together
        # there are a couple of scenarios that can happen at each node
        # both nodes have no children
        # tree1 has children tree2 has no children
        # tree1 has no children tree2 has children
        # both have children
        # so the idea here is probably to do a DFS but it has to happen on both 
        # so for each node check for left and if one has no left connect one to the other if needed
        # same for right
        # but if they both have children then keep traversing down the tree
        # and also add the values together
        # in theory it doesnt matter when the values are added together so we can add them first
        # so ill probably modify root1 rather than root2 and return root1
        
        self.DFS(root1,root2)
        return root1
        