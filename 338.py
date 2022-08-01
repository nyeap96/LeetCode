class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 1
        # 10 11
        # 100 101 110 111
        # 1000 1001 1010 1011 1100 1101 1110 1111
        # 10000 10010 10100 10110 11000 11010 11100 11110
        # 1 2 2 3 2 3 3 4
        # 
        
        # ok so one thing is that for every single odd number is the number before + 1
        # so now i need to figure out how to get all the even numbers
        # for all even numbers 
        # for every power of 2 the number is equal to 1
        # then it follow a pattern that builds on itself
        # 1 2 2 3 2 3 3 4
        
        res = [0]
        for i in range(1,n + 1):
            print(i)
            if i % 2 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[-1] + 1)
        return res
        
        
        
        
        
        
        
        
        