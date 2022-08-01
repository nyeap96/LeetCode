# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # so we need to somehow do this in constant space and o(n) time
        # so we can loop as many time as we want, but how do we store this and check its a palindrome
        # it doesnt say we can't modify the list though
        # so one thing we could do is to make reverse the last half of the list and then compare two lists
        # but i don't really want to do that
        # for now ill do it, cause i can'y think of another method
        
        # first find the length
        length = 0
        
        cursor = head
        while cursor:
            cursor = cursor.next
            length += 1
        
        cursor = head
        for i in range(0,length//2):
            cursor = cursor.next
        #print(cursor.val)
        
        prev = None
        
        while cursor:
            temp = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = temp
        
        cursor = head
        second = prev
            
        
        while cursor and second:
            if cursor.val != second.val:
                return False
            cursor = cursor.next
            second = second.next
        
        return True
        
                        
            
            
        
        
        
        
        
        