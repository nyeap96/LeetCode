class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # not sure what exactly a bijection is but here it says follows the same pattern
        # i assume this means that and given letter can only map to one word
        # unknown if the opposite is true as well though
        # ok so it seems that the opposite is also true so any one word can only be mapped to one letter
        # so we use two dictionaries then
        # one for letter to string
        # another for string to letter
        # could possibly also just use one dictionary
        
        letters = {}
        strings = {}
        
        lList = list(pattern)
        sList = s.split(" ")
        
        if len(lList) != len(sList):
            return False
        
        for i in range(0,len(lList)):
            if lList[i] in letters:
                if sList[i] != letters[lList[i]]:
                    return False
            if sList[i] in strings:
                if lList[i] != strings[sList[i]]:
                    return False
            else:
                letters[lList[i]] = sList[i]
                strings[sList[i]] = lList[i]
            #print(letters)
            #print(strings)
        return True
                
        
        
        
        
        