class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # so the three conditions are as follows:
        # all letters are capital
        # all letters not capital
        # and only first letter is capital
        # so that means that no matter what all letters need to be scanned
        # but you can split into two parts
        # one where the first letter is capital and one where its not capital
        # this can help speed up the process
        
        if len(word) == 1:
            return True
        
        if word[0].isupper():
            # first letter is capital so need to see if all of them are capital or all of them are not capital
            allCap = word[1].isupper()
            
            if allCap:
                for i in range(2,len(word)):
                    if not word[i].isupper():
                        return False
            else:
                for i in range(2,len(word)):
                    if word[i].isupper():
                        return False
        else:
            # first letter not capital so all other not allowed to be capital
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
        return True
                    
        