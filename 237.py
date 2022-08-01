# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # for this problem we don't have access to head so we dont have access to the node before the node to skip
        # this means we can't repoint the previous node to skip the node after it
        # in this case the only choice seems to be to move the values down and delte the last node
        
        nextNode = node.next
        while nextNode:
            print(nextNode.val)
            node.val = nextNode.val
            if nextNode.next == None:
                node.next = None
                nextNode = None
                break
            node = nextNode
            nextNode = nextNode.next
            
        del node
        
        return
        
        
        