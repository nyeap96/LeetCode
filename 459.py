class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # so what i can do here is to set a window size
        # then move the windowSize and keep seeing it is equal what the other parts
        # so first of all if the length of s % windowsize != 0 then it can't do the subtringizing correctly
        # and if it does then you start iterating over the string and comparing
        
        sList = list(s)
        
        
        for windowSize in range(1,len(s)):
            if len(s) % windowSize != 0:
                continue
            else:
                control = sList[0:windowSize]
                i = 0
                while i < len(s):
                    if sList[i:i + windowSize] != control:
                        break  
                    i += windowSize
                
                if i == len(s):
                    return True
                        
        return False
                    