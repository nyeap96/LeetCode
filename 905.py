#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#
#Return any array that satisfies this condition.
#
# 
#
#Example 1:
#
#Input: nums = [3,1,2,4]
#Output: [2,4,3,1]
#Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#Example 2:
#
#Input: nums = [0]
#Output: [0]
# 
#
#Constraints:
#
#1 <= nums.length <= 5000
#0 <= nums[i] <= 5000



class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # so take all even ints and move to front of array
        # easiest thing is probably to evaluate each int and put it into an even or odd array
        # this takes up 2n extra space or even n extra space if done dynamically
        # should only be o(n) or 2/3n if we want to be extra specific
        
        evenInts = []
        oddInts = []
        
        # there are two ways i can think of to identify an odd or even number
        # you can mod by 2
        # and in theory you can also just and the first bit which means just and 1
        # is even and 1 should always be false while odd and 1 should always be true
        # supposedly just doing the bitwise operation is faster, but its harder to understand and probably only like 1 or 2 lines of machine code faster so its probably pointless to do. but ill write it up anyway just to see if its correct
        
        
        #for num in nums:
        #    if num % 2 == 1:
        #       # number is odd
        #        oddInts.append(num)
        #    else:
        #        evenInts.append(num)
        
        # okay so both of them work and are basically the same speed although, speed in leetcode doesnt really mean all that much cause idk how it calculates speed 
        for num in nums:
            if num & 1 == 1:
                oddInts.append(num)
            else:
                evenInts.append(num)
        
        numIndex = 0
        
        for i in range(0,len(evenInts)):
            nums[numIndex] = evenInts[i]
            numIndex += 1
        
        for i in range(0,len(oddInts)):
            nums[numIndex] = oddInts[i]
            numIndex += 1
        
        return nums
        
        
                