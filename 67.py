#Given two binary strings a and b, return their sum as a binary string.
#
# 
#
#Example 1:
#
#Input: a = "11", b = "1"
#Output: "100"
#Example 2:
#
#Input: a = "1010", b = "1011"
#Output: "10101"
# 
#
#Constraints:
#
#1 <= a.length, b.length <= 104
#a and b consist only of '0' or '1' characters.
#Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # so its return their sum as a binary string
        # one way of then doing this would be to convert from binary to decimal, add then convert back to binary
        '''
        decA = int(a,2)
        decB = int(b,2)
        
        res = decA + decB
        
        binRes = bin(res)
        str(binRes)
        return binRes[2:]
        '''
        
        # another way to do this is to iterate over all the values
        # first convert to integers so i can manipulate them
        
        listA = [int(char) for char in a]
        listB = [int(char) for char in b]
        
        if len(listA) >= len(listB):
            long = listA
            short = listB
        else:
            long = listB
            short = listA
        
        carry = 0
        
        result = []
        
        for i in range(0,len(short)):
            temp = long[len(long) - 1 - i] ^ short[len(short) - 1 - i] ^ carry
            carry = (long[len(long) - 1 - i] & short[len(short) - 1 - i]) \
                  | (long[len(long) - 1 - i] & carry) \
                  | (short[len(short) - 1 - i] & carry)
            result.append(temp)
            
        print(result)
        for i in range(len(short),len(long)):
            #print("long = " + str(long[len(long) - 1 - i]))
            
            temp = long[len(long) - 1 - i] ^ carry
            #print("temp = " + str(temp))
            
            carry = long[len(long) - 1 - i] & carry
            #print("carry = " + str(carry))
            result.append(temp)
            #print(result)
            #print()
        
        if carry == 1:
            result.append(1)
        result.reverse()
        
        
        return ''.join(str(num) for num in result)
            
        
            
        