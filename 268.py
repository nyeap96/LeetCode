class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # so lets start by understanding the problem
        # basically the problem is that there is a number that is missing from the string of numbers and you have to figure out which number it is
        # the length of the array will be something and the number go from 0-n
        # this means length of the array will always be n
        # ok so mathematical formula for summation of number can be googled and found to be the following:
        # n(n+1)/2
        # so we can simply identify the biggest number in nums
        # then compare the sum of nums to n(n+1)/2 and subtract
        
        # o(n) to find max value in array
        maxNum = 0
        for i in nums:
            maxNum = max(maxNum,i)
        
        # o(n) to do sum of nums and o(1) to calculate supposedSum
        supposedSum = (maxNum * (maxNum + 1)) // 2
        actualSum = sum(nums)
        
        # now multiple things can happen
        # either it is equal and this means that either a zero or add maxNum + 1
        # or subract to get answer
        if supposedSum == actualSum:
            if 0 in nums:
                return maxNum + 1
            else:
                return 0

        return supposedSum - actualSum
        
        
        
        
        
        