#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#
#Write the code that will take a string and make this conversion given a number of rows:
#
#string convert(string s, int numRows);
# 
#
#Example 1:
#
#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"
#Example 2:
#
#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I
#Example 3:
#
#Input: s = "A", numRows = 1
#Output: "A"
# 
#
#Constraints:
#
#1 <= s.length <= 1000
#s consists of English letters (lower-case and upper-case), ',' and '.'.
#1 <= numRows <= 1000





class Solution:
    
    def addRow (self,startIndex,numRows,myList,s):
        row = ['' for s in range(numRows)]
        for i in range(0,numRows):
            if startIndex + i == len(s):
                break
            row[i] = (s[startIndex + i])
        myList.append(row)
        return
    
    def addDiag(self,startIndex,numRows,myList,s):
        
        zig = ['' for s in range(numRows)]
        
        for i in range(0,numRows - 2):
            if startIndex + i >= len(s):
                break
            zig[numRows - 2 - i] = s[startIndex + i]
            myList.append(zig[:])
            zig[numRows - 2 - i] = ''
        return 
    
    def convert(self, s: str, numRows: int) -> str:
                
        # so most likely the easies thing to do is actually make a matrix, put it in in the zigzag pattern and then iterate over the matrix and build the string
        # so we know the number of rows, but we need to figure out the number of columns
        # this should be solvable using a mathematical function in theory
        # instead maybe lets just build the matrix sideways
        # so instead of an "N" pattern lets do a "Z" pattern
        # that way i just build the matrix as we go instead of predetermining the size
        
        if numRows == 1:
            return s
        
        
        myList = []
        i = 0
        
        while i < len(s):
            self.addRow(i,numRows,myList,s)
            self.addDiag(i + numRows,numRows,myList,s)
            i += numRows + numRows - 2
        
        result = []
        for i in range(0,numRows):
            for j in range(0,len(myList)):
                if myList[j][i] != '':
                    result.append(myList[j][i])
        return ''.join(result)
        
		
		
		
		
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # so theres actually a way better way to do it and its through just labelling each letter to an index
        # so each letter should go into a list and that list will be all letters in a certain row based on index
        # so for "paypalishiring" and n=4 it will look something like 0123432101234
        # then put all same indeces in a list
        
        if numRows == 1:
            return s
        
        myList = [""] * numRows
        print(myList)
        indexList = []
        
        i = 0
        while i < len(s):
            for down in range(0,numRows):
                indexList.append(down)
            for diag in range(numRows - 2,0,-1):
                indexList.append(diag)
            i += numRows + numRows - 2
        print(indexList)
        
        for i in range(0,len(s)):
            myList[indexList[i]] = myList[indexList[i]] + s[i]
            
        result = ""
        
        for string in myList:
            result  = result + string
            
        return result
        