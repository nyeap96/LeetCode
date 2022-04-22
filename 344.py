#Write a function that reverses a string. The input string is given as an array of characters s.
#
#You must do this by modifying the input array in-place with O(1) extra memory.
#
# 
#
#Example 1:
#
#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
#Example 2:
#
#Input: s = ["H","a","n","n","a","h"]
#Output: ["h","a","n","n","a","H"]
# 
#
#Constraints:
#
#1 <= s.length <= 105
#s[i] is a printable ascii character.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers one points to first letter, anotehr to last letter
        back = len(s) - 1
        front = 0
        
        # swap them using a temp which is o(1) memory
        # swap until front is either the same letter as back or in fron of back
        while front < back:
            temp = s[front]
            s[front] = s[back]
            s[back] = temp
            front += 1
            back -= 1
        return s
        
        