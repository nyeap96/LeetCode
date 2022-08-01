import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # so for this problem you should probably use a heap
        # you add your numbers to the heap and keep track of the biggest number unless you hit the third biggest number and return
        # python only has min heap so to make it max heap you invert the values
        
        for i in range(0,len(nums)):
            nums[i] = nums[i] * -1
        
        heap = heapq.heapify(nums)
        res = heapq.heappop(nums)
        thirdMax = 1
        prevVal = res
        
        while nums:
            currentVal = heapq.heappop(nums)
            if currentVal == prevVal:
                continue
            else:
                prevVal = currentVal
                thirdMax += 1
            if thirdMax == 3:
                return currentVal * -1
        return res * -1
            