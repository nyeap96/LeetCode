#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
#You must write an algorithm with O(log n) runtime complexity.
#
# 
#
#Example 1:
#
#Input: nums = [1,3,5,6], target = 5
#Output: 2
#Example 2:
#
#Input: nums = [1,3,5,6], target = 2
#Output: 1
#Example 3:
#
#Input: nums = [1,3,5,6], target = 7
#Output: 4
# 
#
#Constraints:
#
#1 <= nums.length <= 104
#-104 <= nums[i] <= 104
#nums contains distinct values sorted in ascending order.
#-104 <= target <= 104



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # this seems to be a binary search problem
        # so we'll do a form of binary search which takes care of the problem if the target is in the array
        
        start = 0
        end = len(nums) - 1
        mid = int((start + end) / 2)
        
        print(mid)
        
        # binary search is as follows we check the midpoint, if the midpoint is SMALLER than target, then target must be on the RIGHT. if midpoint is BIGGER than target, then target must be on LEFT because array is sorted
        
        while end >= start:
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
            mid = mid = int((start + end) / 2)
        
        # this will either find my number or find the closest to my target on either side i think, so now i just see if i should insert on the left or the right
        
        if nums[mid] < target:
            return mid + 1
        else:
            if mid == 0:
                return mid
            return mid - 1
                
        
        
        
        