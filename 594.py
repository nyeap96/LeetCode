class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # okay so i only have to find the number not the actual subsequence so this makes things a bit easier
        # so what i'm thinking is a dictionary approach which should be o(n)
        # ill first put all keys into the dictionary
        # then for all keys i check to see if key-1 and key+1 is in the dictionary and then add the sum of whichever is bigger
        # do this for all and keep track of a maximum value to return
        
        numDict = {}
        for i in range(0,len(nums)):
            if nums[i] in numDict:
                numDict[nums[i]] += 1
            else:
                numDict[nums[i]] = 1
        
        # ok so now all values and their number of occurrences are in the dictionary now i check each key for key-1 and key+1
        
        maxHSL = 0
        for key in numDict:
            if key - 1 in numDict:
                minusOne = numDict[key - 1]
            else:
                minusOne = 0
            
            if key + 1 in numDict:
                plusOne = numDict[key + 1]
            else:
                plusOne = 0
            
            toAdd = max(plusOne,minusOne)
            if toAdd == 0:
                continue
            maxHSL = max(maxHSL, numDict[key] + toAdd)
            
        return maxHSL