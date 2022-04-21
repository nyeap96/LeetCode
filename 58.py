#Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
#
#A word is a maximal substring consisting of non-space characters only.
#
# 
#
#Example 1:
#
#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.
#Example 2:
#
#Input: s = "   fly me   to   the moon  "
#Output: 4
#Explanation: The last word is "moon" with length 4.
#Example 3:
#
#Input: s = "luffy is still joyboy"
#Output: 6
#Explanation: The last word is "joyboy" with length 6.
# 
#
#Constraints:
#
#1 <= s.length <= 104
#s consists of only English letters and spaces ' '.
#There will be at least one word in s.



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # so this one should be extremely simply for python
        # you split the string into a list of strings using space delimiting
        # the method for that is called split. defulat call uses whitespace as delimiter
        
        #myList = s.split()
        #return len(myList[-1])
        
        
        
        # now lets say split is not allowed
        # so now we have to split it manually
        # so i think now lets do it backwards
        myList = []
        
        # we need to skip leading white spaces
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        
        # so now im at the end of my last word
        # now loop until we see a white space which is the start of my word
        # the order actually doesnt matter so i just append to my list in backwards order
        # then you return the length and thats it
        
        if i < 0:
            return len(myList)
        
        
        
        while s[i] != " ":
            myList.append(s[i])
            i -= 1
            if i < 0:
                break
        return len(myList)
        
        