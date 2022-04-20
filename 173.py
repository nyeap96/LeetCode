#Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#
#BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#int next() Moves the pointer to the right, then returns the number at the pointer.
#Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
#
#You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
#
# 
#
#Example 1:
#
#
#Input
#["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
#[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
#Output
#[null, 3, 7, true, 9, true, 15, true, 20, false]
#
#Explanation
#BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
#bSTIterator.next();    // return 3
#bSTIterator.next();    // return 7
#bSTIterator.hasNext(); // return True
#bSTIterator.next();    // return 9
#bSTIterator.hasNext(); // return True
#bSTIterator.next();    // return 15
#bSTIterator.hasNext(); // return True
#bSTIterator.next();    // return 20
#bSTIterator.hasNext(); // return False
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [1, 105].
#0 <= Node.val <= 106
#At most 105 calls will be made to hasNext, and next.
# 
#
#Follow up:
#
#Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    # so we are looking for o(1) time and o(h) space
    # my first thought was to have next do DFS everytime but that definitely will not be O(1) time
    # the only way to get o(1) time will be to use another data structure
    
    # so when next is called and the node has no child, then we need to somehow go to its parent
    # so the parnet nodes will need to be stored in some data structue
    # stack, queue, heap, hashtable
    # im thinking a stack, or list in python
    # i can put any parent into my stack and go up if i need to
    
    parentList = []
    cursor = TreeNode(-1)
    
    def __init__(self, root: Optional[TreeNode]):
        # its says it should be initialized to something smaller than any BST element and BST elements are between 0 and 10^6    
        parentList = []
        cursor = TreeNode(-1)
        while root.left:
            self.parentList.append(root)
            root = root.left
        self.cursor.right = root
        

    def next(self) -> int:
        if self.cursor.val == -1:
            self.cursor = self.cursor.right
        
        elif self.cursor.right:
            self.parentList.append(self.cursor)
            self.cursor = self.cursor.right
            while self.cursor.left:
                self.parentList.append(self.cursor)
                self.cursor = self.cursor.left
                
        else:
            if self.cursor.val < self.parentList[-1].val:
                self.cursor = self.parentList[-1]
                self.parentList = self.parentList[:-1]
            else:
                self.cursor = self.parentList[-2]
                self.parentList = self.parentList[:-2]
        
        return self.cursor.val    
        
    def hasNext(self) -> bool:
        if self.cursor.right:
            print(self.cursor.right)
            return True
        
        else:
            for node in self.parentList:
                print(self.cursor.val)
                print(node.val)
                print()
                
                if self.cursor.val < node.val:
                    return True
            return False
        
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()