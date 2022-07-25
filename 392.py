class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # you could do 2 pointers, one for s and one for t
        # another way is hashtables
        # put t into a hashtable with the index as the value
        # then keep track of s using indeces
        # hastbale method actually does not work so ill do two pointer method
        
        if not s:
            return True
        
        
        sp = 0
        tp = 0
        
        while sp < len(s) and tp < len(t):
            if s[sp] != t[tp]:
                tp += 1
            else:
                sp += 1
                tp += 1
        
        if sp == len(s):
            return True
        return False
                
                
        
        
        '''
        tDict = {}
        for i in range(0,len(t)):
            if t[i] in tDict:
                tDict[t[i]].append(i)
            else:
                tDict[t[i]] = [i]
        #print(tDict)
        
        # k so i've stored their positions
        # now lets iterate through s
        prevVal = -1
        for i in range(0,len(s)):
            if s[i] in tDict:
                if tDict[s[i]][0] <= prevVal:
                    return False
                else:
                    while tDict[s[i]][0] > prevVal:
                        print(tDict[s[i]])
                        tDict[s[i]] = tDict[s[i]][1::]
                    
                    if not tDict[s[i]]:
                        del tDict[s[i]]
                    else:
                        prevVal = tDict[s[i]][0]
            else:
                return False
        return True
        '''    
        
        