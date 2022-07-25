class Solution:
    '''
    def checkPalindrome(self,s,start,end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    '''
    def longestPalindrome(self, s: str) -> int:
        # i think i can do a two pointer approach here
        # so for any palindrome it must start and end with the same letter meaning that there must be two instances of the same letter in the string
        # so i can have one loop that starts at any letter which will be my starting pointer
        # and then in that loop i can have another loop that iterates backwards. If i find my letter, then see if its a palindrome. that can probably be done with an auxiliary function
        '''
        maxPalindrome = 1
        
        for i in range(0,len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    if self.checkPalindrome(s,i,j) == True:
                        maxPalindrome = max(maxPalindrome,i - j)
        return maxPalindrome
        '''
        
        # ok so i didnt read the problem carefully, its about building palindromes from the available letters not finding palindromes
        # this then becomes a sort of counting problem
        # we store the number of occurences of a letter into a hashtable
        # and for all letters that occur an even number of times they can be part of the palindrome
        # in fact, all numbers happen more than once can be in the palindrome
        # for example, a letter that happens 3 times can use two letters in the palindrome
        
        letterDict = {}
        for i in range(0,len(s)):
            if s[i] in letterDict:
                letterDict[s[i]] += 1
            else:
                letterDict[s[i]] = 1
        
        extra = 0
        maxPalindrome = 0
        for key in letterDict:
            if letterDict[key] % 2 == 0:
                maxPalindrome += letterDict[key]
            else:
                if extra == 0:
                    maxPalindrome += letterDict[key]
                    extra = 1
                else:
                    maxPalindrome += letterDict[key] - 1
        return maxPalindrome
            
        
        
        
        
        
        
        