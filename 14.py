#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".
#
# 
#
#Example 1:
#
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:
#
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
# 
#
#Constraints:
#
#1 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lower-case English letters.





class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # so here we want to iterate over each column of each letter
        # strings are immutable so first we'll wanna convert to list[list]
        
        myList = []
        for i in strs:
            myList.append(list(i))
        
        
        # now we want to identify the shortest word becaseu thats the longest prefix possible this can be done by sorting
        myList.sort(key = len)
        
        # now compare each letter in each word
        prefix = ""
        for col in range(0,len(myList[0])):
            for row in range(1,len(myList)):
                if myList[row][col] == myList[0][col]:
                    continue
                else:
                    return prefix
            prefix += str(myList[0][col])
            
        return str(prefix)
        
        