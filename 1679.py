#You are given an integer array nums and an integer k.
#
#In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
#Return the maximum number of operations you can perform on the array.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,4], k = 5
#Output: 2
#Explanation: Starting with nums = [1,2,3,4]:
#- Remove numbers 1 and 4, then nums = [2,3]
#- Remove numbers 2 and 3, then nums = []
#There are no more pairs that sum up to 5, hence a total of 2 operations.
#Example 2:
#
#Input: nums = [3,1,3,4,3], k = 6
#Output: 1
#Explanation: Starting with nums = [3,1,3,4,3]:
#- Remove the first two 3's, then nums = [1,4,3]
#There are no more pairs that sum up to 6, hence a total of 1 operation.
# 
#
#Constraints:
#
#1 <= nums.length <= 105
#1 <= nums[i] <= 109
#1 <= k <= 109

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # so this seems almost like an extension of the 2 sum problem where you find a pair of numbers that add up to a target
        # but this needs to be extended to happen multiple times
        # this seems like it can be done in n^1 time if i put it into a hash table
        # for any entry, i will see if its complement is in the hash table, if not then add the number into the hash table
        # if it is in the hashtable, remove and add to my count
        
        myDict = {}
        count = 0
        
        for i in range(0,len(nums)):
            # check if complement is in hashtable
            if (k - nums[i]) in myDict:
                myDict[k - nums[i]] -= 1
                if myDict[k - nums[i]] == 0:
                    myDict.pop(k - nums[i])
                count += 1
            else:
                if nums[i] in myDict:
                    myDict[nums[i]] += 1
                else:
                    myDict[nums[i]] = 1
        return count
        
        