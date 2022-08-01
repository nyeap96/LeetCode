# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # esay way to do this is simply traverse twice
        # traverse once to store values in list
        # then traverse again and rewrite them
        
        # first traverse and store values
        dummyHead = head
        myList = []
        while head:
            myList.append(head.val)
            head = head.next
        head = dummyHead
        
        # now traverse again
        i = len(myList) - 1
        while head:
            head.val = myList[i]
            i -= 1
            head = head.next
        return dummyHead
        
        
        