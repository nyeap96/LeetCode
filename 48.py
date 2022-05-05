#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# 
#
#Example 1:
#
#
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]
#Example 2:
#
#
#Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 
#
#Constraints:
#
#n == matrix.length == matrix[i].length
#1 <= n <= 20
#-1000 <= matrix[i][j] <= 1000



class Solution:
    def reverseColumns(self,matrix):
        for i in range(0,len(matrix[0])):
            start = 0
            end = len(matrix) - 1
            while start < end:
                temp = matrix[start][i]
                matrix[start][i] = matrix[end][i]
                matrix[end][i] = temp
                start += 1
                end -= 1
        return
    
    def transpose(self,matrix):
        # in transpose rows become columns
        # and i need o do this one by one
        
        for i in range(0,len(matrix)):
            for j in range(i,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        return
    
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # so it has to be done in place which would mean constant memory usage, so no lists of size n or matrices can be created
        # for n = 1 it stays the same, but it changes when it becomes 2x2
        # for a 2x2 we can observe the following:
        # 1 2 -> 3 1
        # 3 4 -> 4 2
        # so [0,0] -> [0,1], [0,1] -> [1,1], [1,1] ->[1,0], [1,0] -> [0,0]
        # observing the 3x3 matrix i can kinda see that this means the following
        # [0,0]->[0,n - 1]
        # [0,n-1]->[n-1,n-1]
        # [n-1,n-1]->[n-1,0]
        # [n-1,0]->[0,0]
        
        # so now how do i get those values on top bit and side for a 3x3. maybe i can just add 1 every instace of 0
        # [1,1]->[1,n-1] this is not correct i should only add the y coordinate it seems
        # [0,1]->[0,n-1 + 1]
        
        
        # actually looking at the 3x3 it looks like a form of transpose
        # the rotated matrixes first row is a reversed transpose of the first column
        # in transpose, column becomes row so i think what i need to do is first reverse all columns, and then transpose my matrix
        self.reverseColumns(matrix)
        self.transpose(matrix)
        
        return
        