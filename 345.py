class Solution:
    def reverseVowels(self, s: str) -> str:
        # same thing as reverse string just with more steps
        # here we have one pointer that will add the consonants as needed
        # another pointer to add vowels starting backwards
        # this doesnt work cause we lose the data at the front
        # we need to do one pass for vowels and then insert
        
        
        
        index = 0
        vowelList = []
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        for i in range(0,len(s)):
            if s[i] in vowels:
                vowelList.append(s[i])
        res = []
        for i in range(0,len(s)):
            if s[i] in vowels:
                res.append(vowelList[-1])
                vowelList.pop()
            else:
                res.append(s[i])
        return ''.join(res)