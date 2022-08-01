class Solution:
    def isUgly(self, n: int) -> bool:
        #so originally i thought i would have to find all the factors of my number and scan through them
        # but there is actually a better idea
        # what i can do instead is simply divide by my numbers and if it returns not an integer then its not a factor
        
        if n == 0:
            return False
        while n % 5 == 0:
            n = n //5
        
        while n % 3 == 0:
            n = n // 3
        
        while n % 2 == 0:
            n = n // 2
        
        if n != 1:
            return False
        
        return True
        
        
        
        
        