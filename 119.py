class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        triangle = []
        
        for i in range(0,rowIndex + 1):
            if i == 0:
                triangle.append([1])
            elif i == 1:
                triangle.append([1,1])
            else:
                row = [1]
                for j in range(1,i):
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                row.append(1)
                triangle.append(row)
        
        return triangle[len(triangle) - 1]