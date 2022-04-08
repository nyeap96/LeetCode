#Given a string s, find the length of the longest substring without repeating characters.
#
# 
#
#Example 1:
#
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:
#
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:
#
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
#
#Constraints:
#
#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # so i think this can essentially be done witha  two pointer approach to have a sliding window of substrings
        # so you start both front and back at index 0
        # then advance back as long as there is a unique letter. This can be tracked with a hashtable
        # if you find a repeat letter, remove front from the hashtable and then move front forward
        # this might be optimizeable by seeing which is the duplicate letter and advancing from there but that might come with other issues
        
        
        # string length can be 0 first deal with this
        if s == "":
            return 0
        
        front = 0
        back = 0
        
        #turn string into list for easy access
        listStr = list(s)
        
        
        # other structs can be used but hashtable is probably best cause its fast lookup, lookup in lists is stil O(n)
        myDict = {}
        myDict[listStr[back]] = 0
        subStrLen = 1
        back += 1
        
        
        
        while back != len(listStr):
            
            while listStr[back] in myDict:
                del myDict[listStr[front]]
                front += 1
            
            myDict[listStr[back]] = back
            subStrLen = max(subStrLen, back - front + 1)
            back += 1
        return subStrLen
        
        # below is a slightly slower solution because it only either deletes or adds every loop, the above can do both in one loop making it slightly faster
        
        
        
        
        
        
        """
        while back != len(listStr):
            
            if listStr[back] in myDict:
                print("if")
                del myDict[listStr[front]]
                front += 1
                           
            else:
                # here is where back is a unique letter so we add and see if subStrlen should go up. in theory the value of the key is meaningless so just put 0 or something
                print("else")
                myDict[listStr[back]] = 0
                subStrLen = max(subStrLen, back - front + 1)
                back += 1
            print(myDict)
        return subStrLen
        """        
        
        
        
        
        
        
        