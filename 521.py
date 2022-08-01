class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # so the question is what constitues an uncommon subsequence, does having only a single a in one string invalidate all other a's in the other string?
        # okay so actually it seems like the way it works is that unless its an exact match then it can be counted
        # putting in "aba" and "aaba" gives 4 because abaa is not a subsequence of aba not even the aba part counts
        # so its seems like this is simply a problem of finding is a and b are exactly the same i guess?
        if a ==b:
            return -1
        
        return max(len(a),len(b))