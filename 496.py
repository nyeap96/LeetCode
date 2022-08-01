import heapq

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # so lets try to do this in o(n1 + n2) where n1 is length of nums1 and n2 is length of nums2
        # so what im thinking to make this fast is to use a heap
        # i can heapify nums2 and then record all the values and their next greater value as well
        # then traverse over nums1 and then return the next greater values
        
        # oh but im not supposed to change the order of the array so no heap i think
        # instead i think you can do it with just a dictionary
        # so we start at the beginning of array nums
        # we see a number but we don't know what the next bigges number is
        # so we check the next number
        # and two things can happen
        # since nums2 values are unique it can't be equal it can only be greater or lower
        # if its greater then we know the next greater element but then is it bigger than elements before that?
        # you either keep track of bigger elements there or figure out somethiong else
        # maybe we can use a stack instead
        # we put values into the stack if its smaller, then if we find something bigger then we pop off our stack until smaller again, then for everyhing left in the stack its -1
        # if we do this then all values are visited twice at max which is o(n) and then we iterate over nums1 which is o(m)
        
        stack = []
        numDict = {}
        
        for i in range(0,len(nums2)):
            if not stack:
                stack.append(nums2[i])
            else:
                if nums2[i] < stack[-1]:
                    stack.append(nums2[i])
                else:
                    # take advantage of short ciruit to deal with stack
                    while stack and stack[-1] < nums2[i]:
                        val = stack.pop()
                        numDict[val] = nums2[i]
                    stack.append(nums2[i])
        for val in stack:
            numDict[val] = -1
            
        res = []
        for val in nums1:
            res.append(numDict[val])
        return res
                    
        
        
        
        
        
        