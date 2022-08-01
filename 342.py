class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # so for this one, itll be similar to divide by two i guess
        # any number that is a power of four
        # 1  = 1
        # 100 = 4
        # 10000 = 16
        # 1000000 = 64
        # what i can see if that for each power of 4 two zeros are added
        # unfortunately any sort of counting is out because that is a loop
        # instead maybe bitwise anding
        # 10101
        # so we can make a masks that has a 1 at every other bit and see if the number is the same
        # but also have to note that it should only be for numbers that only have single 1 in its number
        # this can be checked by subtracting 1 from the number this is just like what we did when checking for number that have a power of 2
        # if its a power of 4 its also a power of 2 and subtracting 1 from it make it the binary complement
        # so check both conditions and if both true then return true
        # alternating 1010101 number is 1431655765
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            if n & n - 1 != 0:
                return False
            if n & 1431655765 != n:
                return False
        return True
            
        
        
        
        
        
        
        
        
        
        
        
        