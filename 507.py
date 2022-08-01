class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # im thinking you just do the loop itself and see how it can be optimized
        # although one thing i can think of is that you only need to do up to half of n where n is num
        # you simply iterate and when you find i % n is 0 you add to that result and then also i //n as well
        # then you stop at n/2
        # you actually wanna stop after the sqrt and not num/2
        
        if num == 1:
            return False
        
        res = 0
        for i in range(1,int(sqrt(num) + 1)):
            if num % i == 0:
                res += i
                res += num // i    
        res -= num
        print(res)
        
        return res == num
            
            