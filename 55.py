class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # this one seems like it could be a DP problem
        # but also there is a sort of other qay to think about it
        # all values in the array are between 0 and something positive
        # so in theory the only way to not reach the end is if you MUST land on a zero
        # so supposedly i should only need to check if my array has any zeros and if they need to be landed on
        # the question now becomes how do i know i have to land on a zero
        # lets do a sort of greedy algorithm where i calculate at each point the farthest i can go
        # and if i see a zero i check to see if the farthest value is past my zero and if its not then return false
        
        # couple of corner cases
        if len(nums) <= 1:
            return True
        
        if nums[0] == 0:
            return False
        
        # first lets just check for zeros
        if 0 not in nums:
            return True
        
        myList = [nums[0]]
        for i in range(1,len(nums) - 1):
            #print("loop")
            if nums[i] == 0:
                if myList[i - 1] <= i:
                    return False
            
            maxJump = max(myList[i - 1], i + nums[i])
            if maxJump >= len(nums) - 1:
                return True
            else:
                myList.append(maxJump)
            #print(myList)
        
        return True
        
        
        
        