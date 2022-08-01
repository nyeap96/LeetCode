class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # easy way to do this is using a hahstable/dictionary
        # for every element add to the hashtable
        # if elemnt already exists return false
        # this is good solution cause lookup is very fast
        
        myDict = {}
        for i in nums:
            if i in myDict:
                return True
            else:
                myDict[i] = 0
        return False
            
        