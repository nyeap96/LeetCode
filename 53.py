#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
#A subarray is a contiguous part of an array.
#
# 
#
#Example 1:
#
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.
#Example 2:
#
#Input: nums = [1]
#Output: 1
#Example 3:
#
#Input: nums = [5,4,-1,7,8]
#Output: 23
# 
#
#Constraints:
#
#1 <= nums.length <= 105
#-104 <= nums[i] <= 104






class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # this problem has an interesting premise
        # we need to find the subarray that is biggest
        # one thing that i can see right off the bat is that the subarray must end with a positive number
        # it must also start with a positive number
        # i think the algorithm would be the following
        # start by identifying the first positive number
        # then we can add the following numbers
        
        
        
        # actually this is just like the robber house problem. This can be done with dynamic programming
        # what i will do is start with the base case of nums[0] and then replace each value in the array with 
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        testSum = nums[0]
        result = testSum
        for i in range(1,len(nums)):
            testSum = max(testSum + nums[i], nums[i])
            if testSum > result:
                result = testSum
        return result
                
                
            
                
            