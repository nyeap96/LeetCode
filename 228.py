class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # so for this we need to identify ranges, which means breaks in values
        # the array is sorted so we can do a two pointer approach
        # have a pointer at the start, then another pointer that will increment until the outside the range
        # 
        if not nums:
            return None
        
        start = 0
        end = 1
        res = []
        
        while end < len(nums):
            # so if there is a break in continuity
            if nums[end] - nums[end - 1] > 1:
                # if start itself is the range
                if end - start == 1:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[end - 1]))
                start  = end
            end += 1
        if end - start == 1:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[end - 1]))
        
        return res
            
            
            
            
        
        
        