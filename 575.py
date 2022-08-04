class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # ok so alice is only alowed to eat one of each type of candy, denoted by a value
        # and she is also allowed to eat n/2 candies
        # so you essentially return the minimum of n/2 and unique number of candies
        # so you can get a unique number of canides by putting it into a set and returning
        
        uniqueCandy = set()
        
        for i in range(0,len(candyType)):
            uniqueCandy.add(candyType[i])
        
        return min(len(candyType) // 2, len(uniqueCandy))
        