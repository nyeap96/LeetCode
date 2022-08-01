class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # ok so its about checking for dupes and checking if they are farther than k indices apart essentially
        # so it does count if there are more than 1 dupes
        # this means that all dupes need to be considered
        # the best way to do this is probably to use a hashtable
        # save the value of the key and record the indices
        # then at the end subtract the biggest index from the smallest index and return true if it satisfies condition
        
        
        # so first put the values into a hashtable
        myDict = {}
        
        for i in range(0,len(nums)):
            if nums[i] in myDict:
                myDict[nums[i]].append(i)
            else:
                myDict[nums[i]] = [i]
        
        # now loop over all keys and see if last - first index fulfill condition
        
        for key in myDict:
            if len(myDict[key]) == 1:
                continue
            
            for i in range(1,len(myDict[key])):
                if abs(myDict[key][i - 1] - myDict[key][i]) <= k:
                    return True
                
        return False