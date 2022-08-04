class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # so this one is about identifying the biggest three numbers to multiply together
        # the caveat here is that the numbers can be neegative
        # but for the number to still be possitive we are only allowed 2 negative numbers
        # so im thinking what i do here is sort the array by their absolute values and then starting from the back look for the largest value
        # in theory we only need the last 5 values
        # thie is because of negatives
        # if we have too many negatives, can't be used in the valvultation of the maximum value
        # so a product of three numbers is transitive so order doesnt matter and given three numbers there are only a few ways to come back up with a positive number
        # the first is to have all positive numbers
        # the second is to have two negative numbers and one positive number thats it
        # so we should only need to compare these two values to see which is the biggest and return it
        
        if len(nums) == 3:
            return prod(nums)
        
        negNums = []
        posNums = []
        nums.sort()
        for val in nums:
            if val < 0:
                negNums.append(val)
            else:
                posNums.append(val)
        # okay so i have them and they are sorted
        # so if negnums length is less than 2 then no negative numbers are allowed
        # also nums length is guaranteed to be 3 so there are going to be special cases where a number must be negative, this case is when there are exactly two positive numbers and one negative number
        # ok so at this point i've taken care of the base case of only 3 vals in nums
        # special case is when there is less than 3 positive values
        # another special case is when no negative or positive nums
        # when one positive then is positive multiplied by 2 negative
        # when two positive then its positive multipliee by 2 negative again
        if not posNums:
            return negNums[-1] * negNums[-2] * negNums[-3]
        elif not negNums:
            return posNums[-1] * posNums[-2] * posNums[-3]
        
        if len(posNums) < 3:
            return posNums[-1] * negNums[0] *  negNums[1]
        elif len(negNums) < 2:
            return posNums[-1] * posNums[-2] * posNums[-3]
        else:
            # now we have an abundance of number to pick from so we need to do the comparison
            allPos = posNums[-1] * posNums[-2] * posNums[-3]
            twoNeg = posNums[-1] * negNums[0] * negNums[1]
            return max(allPos,twoNeg)
        
        
        
        
        return maxProd
        
        
        
        
        
        
        