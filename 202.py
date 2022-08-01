class Solution:
    def isHappy(self, n: int) -> bool:
        # so this doesnt seem to bad
        # first you start with a loop to do th algorithm of replacing the integer
        # then for each value you get, you put it into a hashtable
        # if the value is ever one, you return true
        # otherwise keep repeating the algorithm and add the the table
        # if you ever see a dupe value in the table then it is in a loop guaranteed because the algorithm is static
        
        
        myDict = {}
        
        
        while n != 1:
            currSum = 0
            while n > 0:
                rem = n%10
                currSum = currSum + (rem ** 2)
                n = n // 10
            n = currSum
            if n in myDict:
                return False
            else:
                myDict[n] = 1
        return True