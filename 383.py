class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # so this one is almost like substring
        # for the ransomenote to be made up of magazine letters, then all the letters in the ransomnote must be in magazine
        # dupes must be accounted for as well
        # so if there are 2 a's in ransomnote then magazine must have two a's as well
        # so put all the items in a hashtable and then compare to each other
        
        ransomDict = {}
        
        for i in range(0,len(ransomNote)):
            if ransomNote[i] in ransomDict:
                ransomDict[ransomNote[i]] += 1
            else:
                ransomDict[ransomNote[i]] = 1
        
        magazineDict = {}
        
        for i in range(0,len(magazine)):
            if magazine[i] in magazineDict:
                magazineDict[magazine[i]] += 1
            else:
                magazineDict[magazine[i]] = 1
        
        for key in ransomDict:
            if key not in magazineDict or magazineDict[key] < ransomDict[key]:
                return False
        return True
        
        