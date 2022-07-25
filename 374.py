# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # this is a binary search problem again
        
        start = 1
        end = n
        mid = (start + end) // 2
        
        while start < end:
            myGuess = guess(mid)
            
            if myGuess == -1:
                end = mid - 1
            elif myGuess == 1:
                start = mid + 1
            else:
                return mid
            mid = (start + end) // 2
        
        return mid
        
        
        
        
        
        
        
        
        