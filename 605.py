class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # so essentially you can only place flowers in every other pot
        # so for any given range between two 1's there should only be like n/2 possible spots assuming best conditions
        # take 1000001 for examples
        # best case is 1010101 so for 5 zeros in a row we get only 2 places to plant
        # add another zero and it makes not difference
        # 10000001 -> 10101001
        # so for every string of zeroa we should add (n - 1)/2 we do n-1 because adding another of the base case of 2 zeros. It should be 0 but it returns one, if we subtract one then it returns what we need.
        # so im thinking maybe just iterate over the array and put indeces into a dictionary
        
        indexDict = {0:[],1:[]}
        
        for i in range(0,len(flowerbed)):
            indexDict[flowerbed[i]].append(i)
        
        if not indexDict[1]:
            return (((len(flowerbed) - 1) // 2) + 1) >= n
        
        res = 0
        if indexDict[1][0] != 0:
            res += indexDict[1][0] // 2
        
        for i in range(1,len(indexDict[1])):
            res += (indexDict[1][i] - indexDict[1][i - 1] - 2) // 2
        
        if indexDict[1][-1] != len(flowerbed) - 1:
            res += ((len(flowerbed)  - 1) - indexDict[1][-1]) // 2
            
            
            
        print(res)
        return res >= n
            
        