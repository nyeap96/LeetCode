# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # so this seems to essentially be a binary search problem
        # however instead of a target value its a target version
        # the only way to know its the target version is if you find the bad version where the previous one is good and the next one is bad
        # or you find a good version where the next one it bad lets actually do this one
        # actually find the opposite of above cause wanna find first bad version
        
        start = 0
        end = n
        mid = (start + end) // 2
        
        while start < end:
            first = isBadVersion(mid)
            second = isBadVersion(mid - 1)
            
            # first one is bad and prev one is good
            if first and not second:
                return mid
            # both versions are bad
            elif first and second:
                end = mid - 1
            # both versions are good
            # no such thing as first is god then second is bad
            else :
                start = mid + 1
            mid = (start + end) // 2
        
        return mid
            
        