class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # is the following, you simpy want to pair up small numbers with small numbers
        # so you sort the array and then pair up starting from the beginning
        
        nums.sort()
        
        res = 0
        for i in range(1,len(nums),2):
            res += min(nums[i],nums[i - 1])
        return res
            
            
        