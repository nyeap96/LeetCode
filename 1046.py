#You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
#We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
#If x == y, both stones are destroyed, and
#If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#At the end of the game, there is at most one stone left.
#
#Return the smallest possible weight of the left stone. If there are no stones left, return 0.
#
# 
#
#Example 1:
#
#Input: stones = [2,7,4,1,8,1]
#Output: 1
#Explanation: 
#We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
#we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
#we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
#we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
#Example 2:
#
#Input: stones = [1]
#Output: 1
# 
#
#Constraints:
#
#1 <= stones.length <= 30
#1 <= stones[i] <= 1000

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # this one is strange i guess, it asks for the smallest posible weight of the last stone.
        # the rules are statis though. So i dont really see how you can have multiple different weights for the last stone
        
        
        # so this seems like it should be done with a heap
        # we want a max heap though so we need to invert stones
        
        heap = [i * -1 for i in stones]
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            # here you perform the rules of the game until 1 or no stones left
            largest = heapq.heappop(heap)
            second = heapq.heappop(heap)
            leftover = largest - second
            if leftover != 0:
                heapq.heappush(heap,leftover)
        
        # now see if the heap is emtpy aka all stones destroyed
        if not heap:
            return 0
        # if not return last stone left
        return heap[0] * -1