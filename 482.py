import string
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # so this seems relatively straighforward
        # you first remove all dashes from the key and then insert a dahs after every k characters going backwards
        # or you just directly build going backwards actually
        sList = []
        
        needDash = 0
        for i in range(len(s) - 1,-1,-1):
            if s[i] != '-':
                sList.append(s[i].upper())
                needDash += 1
            if needDash == k:
                sList.append('-')
                needDash = 0
        sList = sList[::-1]
        
        if not sList:
            return ""
        # now remove leading dash
        if sList[0] == '-':
            sList = sList[1::]
        return "".join(sList)
        
        
        
        