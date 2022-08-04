class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # seems easy enough
        # you treat k as a sliding window and traverse the array with it keeping the average value you find at any point
        # size of nums is guaranteed to be bigger than k so no need to special error checking
        # okay so it needs to be faster
        # in that case what ill do is store it in a single variable
        # start with sum of fir 4 values
        # then everytime you increment add new value and subtract last value
        # this should essentially be 2n instead of k*n
        
        maxSum = sum(nums[0:k])
        trackSum = maxSum
        
        for i in range(k,len(nums)):
            trackSum = trackSum + nums[i] - nums[i - k]
            maxSum = max(maxSum,trackSum)
        
        return maxSum/k