class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # python can do some funny things with this one like the below
        # apparently python doesnt like it when you get to big numbers so this is not a good solution
        
        '''
        test = 0
        for i in range(0,len(digits)):
            test = test*10
            test += digits[i]
        
        test += 1
        print(test)
        
        result = []
        
        while test > 0:
            rem = test % 10
            print(rem)
            result.append(rem)
            test  = int(test/10)
            print(test)
        result.reverse()
        return result
        '''
        # or you can do it in place
        
        carry = 1
        
        for i in range(len(digits) - 1,-1,-1):
            if carry == 1:
                carry = 0
                digits[i] += 1
            
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
            # check to see if we even need to continue
            if carry == 0:
                break
        
        if carry == 1:
            digits.insert(0,1)
        
        return digits
        
        