class Solution:
    def fib(self, n: int) -> int:
        
        n1 = 0
        n2 = 1
        
        if n == 0:
            return n1
        elif n == 1:
            return n2
        
        n3 = n1 + n2
        
        for i in range(2,n + 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3
        
        
        
        