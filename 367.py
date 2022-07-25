class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # one thing i can think of is the brute force method
        # simply take numbers starting from 1 and multiple and see if the value is equal
        # do this until its bigger than the number
        # another thing you can do to make it faster is division maybe
        # well this loop thing is too slow so we need another solution
        '''
        if num == 1:
            return True
        
        for i in range(0,num // 2 + 1):
            if i * i == num:
                return True
        return False
        '''
        
        # 2,4,9,16,25
        # so apparently adding consecutive odd numbers makes up perfect squares so maybe we can just do this instead of multiplication
        
        squares = 0
        oddNum = 1
        
        while squares < num:
            squares += oddNum
            oddNum += 2
        
        if squares == num:
            return True
        return False
        
        
        
        
        
        