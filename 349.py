class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # so it looks like an intersection of two lists is simply any value in both arrays
        # for example 1 the number 2 is in both lists so it is returned
        # for example 2 both 4 and 9 are in both arrays so it is returned
        # order does matter either which can help in speed
        # i would put both array into its own hashmap skipping over the duplicate values
        # then for all keys in one hashmap if its in the other hashmap then add to array to return
        
        dict1 = {}
        for i in range(0,len(nums1)):
            if nums1[i] not in dict1:
                dict1[nums1[i]] = 1
            else:
                continue
        
        dict2 = {}
        for i in range(0,len(nums2)):
            if nums2[i] not in dict2:
                dict2[nums2[i]] = 1
            else:
                continue
        
        # now i have both aray in a hashtable so now compare on to the other
        res = []
        
        for key in dict1:
            if key in dict2:
                res.append(key)
        
        return res
        