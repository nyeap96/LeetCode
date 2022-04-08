#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# 
#
#Example 1:
#
#
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#Example 2:
#
#Input: l1 = [0], l2 = [0]
#Output: [0]
#Example 3:
#
#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]
# 
#
#Constraints:
#
#The number of nodes in each linked list is in the range [1, 100].
#0 <= Node.val <= 9
#It is guaranteed that the list represents a number that does not have leading zeros.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    
    def addCarry(self,addNode,carry):
        if carry == 1:
            addNode.val += 1
        return
    
    def subTen(self,addNode):
        if addNode.val >= 10:
            addNode.val -= 10
            return 1
        return 0
    
#    def finishList(self,list1,list2,myList,carry):
#        # one of the nodes will return null cause it wont exist
#        rCarry = carry
#        if list1:
#            print("list1 leftovers")
#            while list1:
#                addNode = ListNode(0)
#                self.addCarry(addNode,rCarry)
#                addNode.val += list1.val
#                rCarry = self.subTen(addNode)
#                myList.next = addNode
#                myList = myList.next
#                list1 = list1.next
#        
#        elif list2:
#            print("list2 leftovers")
#            while list2:
#                addNode = ListNode(0)
#                self.addCarry(addNode,rCarry)
#                addNode.val += list2.val
#                rCarry = self.subTen(addNode)
#                myList.next = addNode
#                myList = myList.next
#                list2 = list2.next
#        return myList

    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # so we wanna add two numbers digit by digit
        # numbers are in a linked list and are reversed for ease of adding you can just go down the list
        
        #create a new list to return
        
        head = ListNode(0)
        myList = head
        
        list1 = l1
        list2 = l2
        carry = 0
        
        while (list1 and list2):
            addNode = ListNode(0)
            
            #logic to deal with numbers that should carry
            self.addCarry(addNode,carry)
            carry = 0
            
            # add two nodes together and store in my own node
            addNode.val += list1.val + list2.val
            carry = self.subTen(addNode)
                
            myList.next = addNode
            myList = myList.next
            list1 = list1.next
            list2 = list2.next
        
        #the above works nicely when the last digits dont add up past 10 and the numbers are the same size
        # first deal with the numbers not being same size because last digits being more than 10 is present in that issue as well
        # we dont know which one do we check both
        # i orignally tried to put the below logic in its own method but that was causing a lot of issues with regard to the carry and the list itself so its just better for everyone if you just do it explicitly here in the "main" method
        if list1:
            while list1:
                addNode = ListNode(0)
                self.addCarry(addNode,carry)
                addNode.val += list1.val
                carry = self.subTen(addNode)
                myList.next = addNode
                myList = myList.next
                list1 = list1.next
                
        elif list2:
            while list2:
                addNode = ListNode(0)
                self.addCarry(addNode,carry)
                addNode.val += list2.val
                carry = self.subTen(addNode)
                myList.next = addNode
                myList = myList.next
                list2 = list2.next
                
        # now deal with last carry
        if carry == 1:
            addNode = ListNode(1)
            myList.next = addNode
        
        return head.next
        
        
        
        
        
        
        
        
        
        
        
        
        