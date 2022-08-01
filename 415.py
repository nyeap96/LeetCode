class Solution:
    def strToInt(self,snum):
        numDict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        res = 0
        for i in range(0,len(snum)):
            res = res * 10
            res += numDict[snum[i]]
        return res
        
    def addStrings(self, num1: str, num2: str) -> str:
        # create a function to convert the numbers from str to int
        # you can just make a hashtable that reads over the numbers and then converts
        
        val1 = self.strToInt(num1)
        val2 = self.strToInt(num2)
        return str(val1 + val2)
        