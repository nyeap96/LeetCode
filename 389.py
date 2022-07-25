class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # this can be done with two hashtables
        # you use letters as keys and then number of occurneces as value
        
        sDict = {}
        for i in range(0,len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1
                
        tDict = {}
        for i in range(0,len(t)):
            if t[i] in tDict:
                tDict[t[i]] += 1
            else:
                tDict[t[i]] = 1
        
        # now compare
        for key in tDict:
            if key not in sDict:
                return key
            else:
                if sDict[key] != tDict[key]:
                    return key
            
        return