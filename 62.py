class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # classic DP problem to solve
        # the robot can move only down or right
        # so for the top row the entire thing comes out to one
        # the first column is also all ones
        
        #initialize grid of size m-1,n-1
        grid = [[1] * n for i in range(0,m)]
        
        # now for all values, excluding the first values, we know that for each one there are two way to reach a square
        # one from the top and one from the left
        # so this means for each square if we add both top and left then we can get the number of ways to reach the square
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i -1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]
            
        
        