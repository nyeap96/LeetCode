class Solution:
    def sideofWater(self,grid,row,col):
        up = 0
        right = 0
        down = 0
        left = 0
        
        if row - 1 < 0:
            up = 1
        else:
            up = grid[row - 1][col] ^ 1
        
        if row + 1 >= len(grid):
            down = 1
        else:
            down = grid[row + 1][col] ^ 1
        
        if col - 1 < 0:
            left = 1
        else:
            left = grid[row][col - 1] ^ 1
        
        if col + 1 >= len(grid[0]):
            right = 1
        else:
            right = grid[row][col + 1] ^ 1
        
        return up + right + down + left
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # so for each piece of land you simply just count how many sides are touching water and then you should b done, being at the end of the array or beginnin counts as touching water as well
        # this can be done in o(m*n) but you also might be able to do it faster through some speical methods of identifying land
        res = 0
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1:
                    #print([i,j])
                    res += self.sideofWater(grid,i,j)
        return res
        
        
        