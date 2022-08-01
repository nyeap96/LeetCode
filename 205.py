class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # first of all to optimize i can check if legnth is the same. if not then i can return false
        # if both strings are empty then return true
        
        
        if (not s) and (not t):
            return True
        elif s and not t:
            return False
        elif not s and t:
            return False
        else:
            if len(s) != len(t):
                return False
        
        # no two characters may map to the same character
        # so we can add both letters as the key maybe
        # 
        
        myDict = {}
        exclude = {}
        for i in range(0,len(s)):
            if s[i] not in myDict:
                if t[i] in exclude:
                    return False
                else:
                    myDict[s[i]] = t[i]
                    exclude[t[i]] = 1
            else:
                if myDict[s[i]] != t[i]:
                    return False
        return True