
#Given a string s, return the longest palindromic substring in s.
#
# 
#
#Example 1:
#
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
#Example 2:
#
#Input: s = "cbbd"
#Output: "bb"
# 
#
#Constraints:
#
#1 <= s.length <= 1000
#s consist of only digits and English letters.


# this solution can probably be optimized if you save the the start and end variables and ignore all letters in between or some form of variation on that





class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # so there are a couple of interesting scenarios going on here
        # a single letter is a palindrome of length one
        # i would say palindrom fall into two categoried as well
        # ones that share a base letter and one that does
        # so 'a' is a palindrome that shares a base letter the middle letter of the palindrome much like a median number in a set with an odd size
        # 'bb' is a palindrome that does not share a base letter, there isnt quite a center kind of like how in a set with even size, the median is the average of the TWO center numbers
        
        
        # so i think the algorithm should then be as such
        # each letter is a palindrome. And if we extend this to the letters on each side, if the letters on each side are a palindrome, then you repeat until you find a nonpalindrome
        # but first you need to determine if its a shared letter palindrome or not first. I think we can this by just checking the outside letters first
        # so 'babad' for 'a' at index 1 you check index 1-1 and index 1+1 and see if its a palindrome and it is so you save it as a string
        # but for 'cbbd' at index 1 you check 1-1 and index 1+1 and see if its a palindrome. Its not but index 1-2 is a palindrome so you save that and then follow the algorithm again
        # determining if is shared center or not should only happen once
        
        
        stringList = list(s)
        print(stringList)
        
        if len(s) <= 1:
            return s
        result = stringList[0]
        
        
        for i in range(1,len(stringList)):
            testString = stringList[i]
            
            
            # this happens first to determine if shared letter or not
            start = i - 1
            end = i + 1

            # the below is not working for even length strings of the same letter because it is trying to be greedy and that is messing things up
            # another approach i can think of is to simply account for large strings of the same letter because those are all palindromes
            
            #if stringList[start] == stringList[end]:
            #    testString = stringList[start] + testString + stringList[end]
            #    start -= 1
            #    end += 1
            #elif stringList[start] == stringList[i]:
            #    testString = stringList[start] + testString
            #    start -= 1
            #elif stringList[end] == stringList[i]:
            #    testString = testString + stringList[end]
            #    end += 1
            
            # im seeing issues with the below due to not short circuiting, if i rearrange the conditions it should work, but i dont quite like that, i should have started with something that wouldnt have generated a runtime error
            
            #while stringList[start] == stringList[i] and start >= 0:
            #    testString = stringList[start] + testString
            #    start -= 1
            #    
            #while stringList[end] == stringList[i] and end < len(stringList) - 1:
            #    testString = testString + stringList[end]
            #    end += 1
            
            while start >= 0:
                if stringList[start] == stringList[i]:
                    testString = stringList[start] + testString
                    start -= 1
                else:
                    break
    
            while end <= len(stringList) - 1:
                if stringList[end] == stringList[i]:
                    testString = testString + stringList[end]
                    end += 1
                else:
                    break
            
            
            
            # need error checking for trying to go outside of array
            # now expand out
            # i used to have start and end here but it needs to be moved earlier and updated in the ifs above
            while start >= 0 and end <= len(stringList) - 1:
                if stringList[start] == stringList[end]:
                    testString = stringList[start] + testString + stringList[end]
                else:
                    break
                start -= 1
                end += 1
            
            if len(testString) > len(result):
                result = testString
        return result
            
        
        