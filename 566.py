class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # okay so first we need to see if reshaping the matrix is legal
        # in this case im guessing legal means that the number of entries in the original array will fill the modified array exactly, no empty or extra elements
        # so row and col are passed in
        # just need to do the multiplication to tell if it should even be legal first of all.
        if len(mat) * len(mat[0]) != r * c:
            return mat
        if len(mat) == r:
            return mat
        
        
        # ok so its legal so now we need to iterate and add
        # first initialize a matrix
        newMat = [[-1] * c for i in range(0,r)]
        # okay now we ned to move the value from one array to the other
        # its possible to do it in place, but its really annoying to do because youd have to consatntly check for updates on when to move to a new row in one of the matrices
        # instead ill just put all the values in an array and then transfer over
        
        transferArray = []
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                transferArray.append(mat[i][j])
        
        arrayIndex = 0
        for i in range(0,r):
            for j in range(0,c):
                newMat[i][j] = transferArray[arrayIndex]
                arrayIndex += 1
        
        return newMat