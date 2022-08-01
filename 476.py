class Solution:
    def findComplement(self, num: int) -> int:
        # get binary number into a list and then xor 1 over all bits
        binaryNum = list(bin(num))
        binaryNum = binaryNum[2::]
        
        for i in range(0,len(binaryNum)):
            binaryNum[i] = int(binaryNum[i]) ^ 1
        
        res = 0
        for i in range(0,len(binaryNum)):
            res = res << 1
            res += binaryNum[i]
        return res