class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCons = 0
        res = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                maxCons += 1
            else:
                res = max(res,maxCons)
                maxCons = 0
        res = max(res,maxCons)
        return res