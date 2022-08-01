class Solution:
    def countSegments(self, s: str) -> int:
        # this is the easy python way of doing it
        # next i do it without the python stuff
        #listStrings = s.split()
        #return len(listStrings)
        
        # just count number of spaces and add one
        # not just that actually, need to make sure there are other characters in the string
        space = 0
        if s == "":
            return space
        
        for i in range(1,len(s)):
            if s[i] != ' ' and s[i -1] == ' ':
                space += 1
        if s[0] == ' ':
            space -= 1
        return space + 1
        