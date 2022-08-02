import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # so maybe we'll divide by k-1 for what we need
        # oh ok i see so the examples did not showcase the problem well
        # the arrays are all sorted, but one array is not strictly bigger than a previous array
        # so you probably have to iterate over all arrays or something like that
        # so we wanna do this in constant memory
        # and maybe o(n) time
        # ok so maybe we do want to use a heap here then
        # we can heapify all the values and simply pop the smallest one every time until k is 0
        # this would be a o(m*n) solution with no extra memory
        
        for row in matrix:
            heapq.heapify(row)
        
        # so now they're all heapified
        # now we create a loop to get the smallest value and pop
        
        while k > 0:
            nextMinRow = 0
            while not matrix[nextMinRow]:
                nextMinRow += 1
            for row in range(0,len(matrix)):
                if matrix[row]:
                    if matrix[row][0] < matrix[nextMinRow][0]:
                        nextMinRow = row
                else:
                    continue
            res = heapq.heappop(matrix[nextMinRow])
            k -= 1
        return res
        
        
        
        
        
        
        
        