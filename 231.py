class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # the easiest way to do this is using bit shifting
        # take a int value 1 which is 2**0 and then check if it is ==n
        # if not then shift left and repeat
        # another way which doesnt use a loop is to siply store all the values in a hastable and then do hashtable lookup which would be fast
        # but that method is also tedious and would require looking up all the powers of two
        # but actually going back to my first methos is even better
        # instead of comparing n to a comparator
        # i can just check and see if n only has a singular 1 in its binary value
        # if not then its not a power of 2
        # only question is how do i do it without a loop
        # one thing to note is no leading 0s do i don't really have to worry about values after my leftmost 1
        # but i need to figure out about the ones all on the right
        # i could try to figure out what the values to achieve all 1's and then compare to that maybe
        # but that won't work itll just return the same number
        # what about the binary reverse of the number(no, technically still a loop i think)
        # ok so one thing to note is that for any power of two it is a binary 1 with a bunch of zeros after it
        # so if we subtract one from it we lose the one and then get all 1s
        # then anding those two together gives us zero
        # but for any number above it then it keeps the 1
        # so maybe we can do num & num-1
        # 
        
        
        if n == 0:
            return False
        
        if (n & n-1) > 0:
            return False
        elif (n & n-1) == 0:
            return True
        else:
            return False
        
        