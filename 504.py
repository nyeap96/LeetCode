class Solution:
    def convertToBase7(self, num: int) -> str:
        # luckily the number is in base 10 already
        # so what we wanna do is change the number from base 10 to base 7
        # this can be done similary to converting to binary
        # when conveting to binary you divide by two and then remainder is the bit
        # then shift and divide again and repeat
        
        if num == 0:
            return "0"
        
        neg = 0
        if num < 0:
            neg = 1
            num *= -1
        binList = []
        while num > 0:
            rem = num % 7
            binList.append(str(rem))
            num = num // 7
        binList = reversed(binList)
        
        if neg:
            res  = "-"
        else:
            res = ""
        return res + "".join(binList)
        