# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # so for this im thinking first start with two pointers a current and prev pointer
        # if current points to val then make prev point to current.next
        # this should take care of all values except if head is val
        # just put something in at the end where if head is val the head = head.next
        
        
        if not head:
            return head
        
        prev = head
        curr = head.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next
        
        if head.val == val:
            return head.next
        else:
            return head