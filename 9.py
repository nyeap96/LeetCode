#Given an integer x, return true if x is palindrome integer.
#
#An integer is a palindrome when it reads the same backward as forward.
#
#For example, 121 is a palindrome while 123 is not.
# 
#
#Example 1:
#
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
#Example 2:
#
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#Example 3:
#
#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
#
#Constraints:
#
#-231 <= x <= 231 - 1
# 
#
#Follow up: Could you solve it without converting the integer to a string?





class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # all negatives are not palindromes. single digit numbers are all palindromes. special cases for both
        
        # all negatives
        if x < 0:
            return False
        # all negatives taken care of now all single digits
        if x >= 0 and x < 10:
            return True
        
        # so we now need to reverse the number
        xRev = 0
        xCopy = x
        
        
        while xCopy > 0:
            # we can extrace digit by digit by taking remainders and dividing
            remainder = int (xCopy % 10)
            xRev = (xRev * 10) + remainder
            xCopy = int(xCopy / 10)
        
        if xRev == x:
            return True
        return False
        
        
        