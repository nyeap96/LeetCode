class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if i remember correctly this is one of those puzzle problems
        # any number xord with itself is zero so if you xor everything in the array ou are left with only the odd number out
        res = 0
        for i in nums:
            res = res ^ i
        return res
        
        
        
        
        