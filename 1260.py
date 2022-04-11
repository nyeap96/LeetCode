#Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
#
#In one shift operation:
#
#Element at grid[i][j] moves to grid[i][j + 1].
#Element at grid[i][n - 1] moves to grid[i + 1][0].
#Element at grid[m - 1][n - 1] moves to grid[0][0].
#Return the 2D grid after applying shift operation k times.
#
# 
#
#Example 1:
#
#
#Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
#Output: [[9,1,2],[3,4,5],[6,7,8]]
#Example 2:
#
#
#Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
#Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
#Example 3:
#
#Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
#Output: [[1,2,3],[4,5,6],[7,8,9]]
# 
#
#Constraints:
#
#m == grid.length
#n == grid[i].length
#1 <= m <= 50
#1 <= n <= 50
#-1000 <= grid[i][j] <= 1000
#0 <= k <= 100


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        # this problem is an interesting one. Its abour shifting the grid, but I don't think you really have to actually move around any values just do some math to achieve the same thing.
        # unfortunately seeing example 2 the answer is not just math, you may have to actually do some shifting, if you don't have to then you have to do math on positions rather than values themselves so that you can change around positions
        # matrix size is variable, but maybe what i can do is assign a number to each position and then recalculate the position b adding k
        
        
        row = len(grid)
        col = len(grid[0])
        size = row * col
        
        linearIndex = list(range(size))
        # now you can calculate rotation. rotation above k times is just looping rotations. so if you take remainders you can distill it down to a smaller number
        rotate = k % len(linearIndex)
        
        # now you add rotate to the linear index to get where the new postitions are, then if a position is too big, subtract size
        
        for i in range(0,len(linearIndex)):
            linearIndex[i] -= rotate
            if linearIndex[i] <= -1:
                linearIndex[i] += size
        # okay so now we have relative positions, we can turn these into actual grid coordinates and replace with actual values
        for i in range(0,len(linearIndex)):
            x = int(linearIndex[i] / col)
            y = int(linearIndex[i] % col)
            linearIndex[i] = grid[x][y]
        
        # now we just translate this linear index into a grid
        result = []
        
        for i in range(0,row):
            resRow = []
            for j in range(0,col):
                resRow.append(linearIndex[i*col + j])
            result.append(resRow)
        # the above can probably be optimized by actually instantiating a grid instead of a linearindex, runtime will be some factor of n*m faster
        return result
        
        
        
        
        