class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # so for each operation it goes increments everything in the row-1 col-1 area
        # so for [2,2] it increments everything in the 0-1 inclusive row and 0-1 inclusive column
        # so i think we only need to scan for the min value of row and min value of column
        # because the min row means everything in that row and every row before was always incremented
        # but not every column was incremented so we need to account for that as well
        
        minRow = m
        minCol = n
        
        for op in ops:
            minRow = min(minRow,op[0])
            minCol = min(minCol,op[1])
        return minRow * minCol
        