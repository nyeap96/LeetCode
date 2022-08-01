class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # so this seems like it can be solved using DP but it also may not even need quite that
        # for each time t there are only really a few situations that can happen
        
        # teemo does not attack and ashe is not poisoned
        # teemo does not attack and ashe is poisoned
        # teemo does attack and ashe was not poisoned
        # teemo does attacj and ashe was poisoned
        
        # for each situation the following situations should happen
        # not counted
        # counted
        # counted and timer is set
        # counted and timer is set
        
        # so i think the easiest way to do this is to just iterate through the array and keep track of stuff
        # for each time we can be certain of what happened before then and calculate the poison time
        if duration == 0:
            return 0
        
        poisonTime = 0
        
        for i in range(1,len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] > duration:
                poisonTime += duration
            else:
                poisonTime += timeSeries[i] - timeSeries[i -1]
        return poisonTime + duration
        