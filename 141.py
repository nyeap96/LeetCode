# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # the key here is the loops
        # if there is a loop then no matter what as long as you go to the next pointer it will exist
        # so we can have two pointers
        # one at the head and one starting at hed.next
        # we can make head.next hop two positions per loop
        # and we can make head hop one position per loop
        # this avoids a permature match because one of two situations will happen
        # first is that there is no loop and the pointer starting at head.next runs off
        # second is that there is a loop and eventually both pointers will point to the same object
        
        
        if not head:
            return False
        if head.next == head:
            return True
        
        
        cursor1 = head
        cursor2 = head.next
        
        while cursor1 and cursor2:
            
            print(cursor1.val)
            print(cursor2.val)
            if cursor1 == cursor2:
                return True
            
            cursor1 = cursor1.next
            if not cursor2.next or not cursor2.next.next:
                return False
            else:
                cursor2 = cursor2.next.next
        
        return False
        
        
        
        
        
        