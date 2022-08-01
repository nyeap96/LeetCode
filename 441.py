class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        level = 1
        res = 0
        
        while n >= level:
            n -= level
            level += 1
            res += 1
            
        return res
        
        
        