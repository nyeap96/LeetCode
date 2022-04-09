#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# 
#
#Example 1:
#
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]
#Example 2:
#
#Input: nums = [1], k = 1
#Output: [1]
# 
#
#Constraints:
#
#1 <= nums.length <= 105
#k is in the range [1, the number of unique elements in the array].
#It is guaranteed that the answer is unique.
# 
#
#Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so this one seems like it can be done in 2 loops. one for a hashtable and then another tofind k most frequent elements
        
        # start with inserting into hashtable
        
        myDict = {}
        
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        
        # we do reversed for ease of sorting then we can just call sort on our list since it sorts by first element
        # looks like a tuple can't be sorted, might be because tuples are immutable so we need to convert tuple to list first
        myList = list(myDict.items())
        
        for i in range(0,len(myList)):
            myList[i] = list(myList[i])
            myList[i].reverse()
        myList.sort()
        
        results = []
        # now extract only interested values
        for i in range(len(myList) - k, len(myList)):
            results.append(myList[i][1])
        return results