class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # okay so the three constraints mean the following
        # that the rectangle will always be tall because its l >= w
        # and the difference betwen l and w should be as small as possible
        # the area must be equal as well
        
        # so i think you should be able to do the following
        # start with l = w which means l should be l/2 but if its not an integer then skip
        # then you keep bringing l down until you find an l % n == 0 and then return that value
        # so its actually not half but square root which is hard to calculate
        # so instead what ill do is to just iterate backwards and store all results i see until w > l then return
        
        # above is false meaning l and w are not the same so you have to start iterating
        
        res = [-1,-1]
        
        for i in range(area , 0, -1):
            if area % i == 0:
                if (area // i) > i:
                    break
                else:
                    res = [i,area // i]
            
            
        return res