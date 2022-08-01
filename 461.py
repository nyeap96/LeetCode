class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # so for each bit, compare the bits and see how many same order bits are different
        # this can be done by comparing each last order bit and then if xor returns one then add to result
        # so need to extract both first order bits by anding with one
        
        res = 0
        while x > 0 or y > 0:
            xBit = 1 & x
            yBit = 1 & y
            res += xBit ^ yBit
            
            x = x >> 1
            y = y >> 1
        return res
        
        
        
        
        
        
        