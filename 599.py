class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # ok so this can be done using hashtables
        # i only actually need one i think
        # ill first put one list into a hashtable with the name as a key and the index as a value
        # then i can iterate over the other one while checking and keeping track of the minimum index score 
        # all strings in l1 and l2 are unique so just put them in
        
        
        oneDict = {}
        
        for i in range(0,len(list1)):
            oneDict[list1[i]] = i
            
        # ok so now create a minIndex which can be the max index number
        # there is always an answre so no need ot error check, if we need it though you could set mindex to be len of both lists added +1 which is an impossible number for an answer
        minIndex = len(list1) + len(list2)
        resNames = []
        
        # now iterate over other list
        # no way to know what is minindex until end and how many are minindex
        # so i rewrite all shared values into its index sums and will iterate one last time at the end to search for minindex
        # ill just put it into a shared dict to avoid some other overlap with no shared values
        sharedDict = {}
        for i in range(0,len(list2)):
            if list2[i] in oneDict:
                minIndex = min(minIndex,oneDict[list2[i]] + i)
                sharedDict[list2[i]] = oneDict[list2[i]] + i
        
        resNames = []
        for key in sharedDict:
            if sharedDict[key] == minIndex:
                resNames.append(key)

        return resNames
            
            