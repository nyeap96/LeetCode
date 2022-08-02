class Solution:
    def checkRecord(self, s: str) -> bool:
        # ok so this is a singular student so we only need to return true of false
        # only return true if two things happened
        # one never absent more than once
        # two not late three times in a row
        # we can take care of each in one loop
        # probably no need for a hashtable
        
        # first count absences can maybe extend to do lates as well
        absences = 0
        for i in range(0,len(s)):
            if s[i] == 'A':
                absences += 1
                if absences >= 2:
                    return False
            
        if len(s) < 3:
            return True
        else:
            for i in range(2,len(s)):
                if s[i - 2:i + 1] == 'LLL':
                    return False
        return True
                    
        
            
        
        
        
        
        
        