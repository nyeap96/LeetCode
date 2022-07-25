class Solution:
    def firstUniqChar(self, s: str) -> int:
        # ah i see so its checking for the first letter that doesnt have a duplicate later
        # so for example one 'leetcode' only has one l so its that one
        # then for loveleetcode l happens multiple times and as does o so its v's index that is returned
        # is there a way to do it in one pass?
        # my first thought is hashtable
        # put them all into a hashtable but then how can you pinpoint which letter happens first?
        sDict= {}
        
        for i in range(0,len(s)):
            if s[i] in sDict:
                sDict[s[i]][1] += 1
            else:
                sDict[s[i]] = [i,1]
        #print(sDict)
        
        res = len(s)
        for key in sDict:
            if sDict[key][1] == 1:
                res = min(res,sDict[key][0])
        if res == len(s):
            return -1
        return res
        
                
                
        
        
        
        
        
        
        