class Solution:
    def toHex(self, num: int) -> str:
        # so hex is base 16 so to convert from base 10 to base 16 we simply take our base 10 number and divide by 16
        # 26/16 = 1 remainder 10 which become 1a
        # for the value 300 it is 18 remainder 12
        # 18 can still be divided again
        # go it becomes 12c
        
        # so now we turn this into an algorithm
        # create array yo store my number
        
        if num == 0:
            return str(num)
        
        hexDict = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        hexVal = []
        # got this from someone elses solution
        # the reason this works is because it essentially uses a 33rd bit to use as a dummy
        if num < 0:
            num += 2 ** 32
        
        while num > 0:
            rem = num % 16
            if rem >= 10:
                hexVal.append(hexDict[rem])
            else:
                hexVal.append(str(rem))
            num = num // 16
        hexVal.append(str(num))
        hexVal.reverse()
        hexVal = hexVal[1::]
        
        return ''.join(hexVal)
        