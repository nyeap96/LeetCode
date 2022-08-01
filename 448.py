class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # couple of way you can do this, first way is to sort the array and then do something where you track indeces and values to see what values are missing
        # this would require sorting which is nlogn speed
        # a faster way would be to put the values into a hashtable and then iterate seeing what values are missing this would be n+m speed where m is len(nums) and n is max of nums + 1
        # this would effectively be n speed because n will always be bigger than m
        # whoops didnt see the follow up and just solved it first, but for this one i would probably do some kinda pointer method maybe
        # have an variable to keep track of index and then note which indexes are not in the array
        
        valDict = {}
        
        for val in nums:
            if val in valDict:
                continue
            else:
                valDict[val] = 1
        
        
        missing = []
        
        for i in range(1,len(nums) + 1):
            if i not in valDict:
                missing.append(i)
            else:
                continue
        
        return missing
        
        
        