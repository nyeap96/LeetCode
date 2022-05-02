#You are climbing a staircase. It takes n steps to reach the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# 
#
#Example 1:
#
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Example 2:
#
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
# 
#
#Constraints:
#
#1 <= n <= 45



class Solution:
    def climbStairs(self, n: int) -> int:
        # this is one of those dynmic programming problems
        # the idea is to start with some base cases
        # for n = 1 there is only one way to get the the top
        # for n = 2 there is two ways to get to the top
        # but for n=3 there is multiple ways to get there
            # we can do first step then jump 2 or first step jump one, but there is also the fact that for n=2 we have two ways yo get there
        # so for n=3 it should be n-1 + n-2 ways to get there
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        myList = [1,2]
        
        for i in range(2,n):
            myList.append(myList[i - 2] + myList[i - 1])
        
        return myList[len(myList) - 1]