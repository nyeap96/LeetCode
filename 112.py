# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self, root,target):
        
        if not root:
            return False
        # target number is reached now check for children
        #print(target - root.val)
        if target - root.val == 0:
            #print("possible correct")
            if not root.left and not root.right:
                return True
        # theres room to check numbers still
        return self.DFS(root.left,target - root.val) or self.DFS(root.right,target - root.val)
            
        
        
        
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # ok so this problem is obviously recursive but how
        # i think its like this
        # the top node obviously needs to take away its valule from the targetsum
        # and this should happen recursively until you reach 0
        # so write a DFS that subtracts from the value and passes that subtraced value down the tree
        # each time you go down it subtracts
        # return True if you have a node with no children that also equals 0
        # otherwise return false
        return self.DFS(root,targetSum)
        
        
        
        