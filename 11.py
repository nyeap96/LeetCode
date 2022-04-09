#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
#Return the maximum amount of water a container can store.
#
#Notice that you may not slant the container.
#
# 
#
#Example 1:
#
#
#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#Example 2:
#
#Input: height = [1,1]
#Output: 1
# 
#
#Constraints:
#
#n == height.length
#2 <= n <= 105
#0 <= height[i] <= 104


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # sart with ends of the things
        
        front = 0
        back = len(height) - 1
        maxWater = (back - front) * min(height[back],height[front])     # min is done here because all water above min spills out
        
        
        # this can be optimized with the following premise. Since, we start at the ends the width can only get smaller. This means that the only way to get more water is if the height becomes taller. so we can be greedy and only take bigger the bigger height when comparing the next front or next back
        
        while (front != back):
            maxWater = max(maxWater, (back - front) * min(height[back],height[front]))
            if height[front] >= height[back]:
                back -= 1
            else:
                front += 1
        return maxWater
        
        
        
        
        
        
        