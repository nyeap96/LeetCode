# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # im thinking a n*m solution where you put list A in a a dictionary and find the first thing in list B that is in the dict, first thing found is intersection
        # if nothing in ListB is in list A then no intersection
        
        '''
        myDict = {}
        
        cursorA = headA
        while cursorA:
            myDict[cursorA] = cursorA.val
            cursorA = cursorA.next
        
        cursorB = headB
        while cursorB:
            if cursorB in myDict:
                return cursorB
            else:
                cursorB = cursorB.next
        
        return None
        '''
        
        # so now we can try a solution that is o(1) memory
        # this requires doing a two pointer solution probably
        # i could maybe get the lengths of my lists and then start from the same relative index and increment one side at a time until at the they both point to the same node
        # so for the first example i could loop through a and b and get the lenths
        # then start at the first node for A and the second node for B
        # then check if a.next == b.next
        # if not then increment both
        
        if headA == headB:
            return headA
        
        cursorA = headA
        cursorB = headB
        lenA = 0
        lenB = 0
        
        while cursorA:
            lenA += 1
            cursorA = cursorA.next
        
        while cursorB:
            lenB += 1
            cursorB = cursorB.next
        
        cursorA = headA
        cursorB = headB
        
        if lenA >= lenB:
            long = 0
        else:
            long = 1
        
        if long == 0:
            for i in range(lenA - lenB):
                cursorA = cursorA.next
        else:
            for i in range(lenB - lenA):
                cursorB = cursorB.next
       
        if cursorA == cursorB:
            return cursorA
        while cursorA.next != cursorB.next:
            cursorA = cursorA.next
            cursorB = cursorB.next
            
        return cursorA.next