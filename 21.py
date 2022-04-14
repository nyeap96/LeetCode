#You are given the heads of two sorted linked lists list1 and list2.
#
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
#Return the head of the merged linked list.
#
# 
#
#Example 1:
#
#
#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#Example 2:
#
#Input: list1 = [], list2 = []
#Output: []
#Example 3:
#
#Input: list1 = [], list2 = [0]
#Output: [0]
# 
#
#Constraints:
#
#The number of nodes in both lists is in the range [0, 50].
#-100 <= Node.val <= 100
#Both list1 and list2 are sorted in non-decreasing order.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        # basic errro checking and base case optimization
        if not list1:
            return list2
        if not list2:
            return list1
        
        # at first i created a new node, but now i wanna see if i can optimize and create no new object
        # create pointer of head which points to lowest val. lists are already sorted so i just follow logic i do in loop
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        # keep a copy to return
        result = head
        
        
        # now i start splicing together
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        else:
            head.next = list2
            
        return result