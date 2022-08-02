class Solution:
    
    def reverseSet(self,sList):
        start = 0
        end = len(sList) - 1
        
        while start < end:
            temp = sList[start]
            sList[start] = sList[end]
            sList[end] = temp
            start += 1
            end -= 1
        
        return sList
            
        
    
    def reverseStr(self, s: str, k: int) -> str:
        # okay so for the firs example its "abcdefg" becomes "bacdfeg"
        # what happened is the first two letters reversed
        # then the next two letters did not get reversed
        # then the two after that did get reversed
        # and if k were to be equal to 3 then you reverse the first three ignore the next three etc
        
        # so first lets start by reversing in sets of 3
        # then have  function that reverses for me like in a previous problem
        # then have a loop that increments by k everytime
        
        # get a list of characters so i can actually changed the order
        sList = list(s)
        
        toReverse = 1
        for i in range(0,len(sList),k):
            if toReverse:
                sList[i:i + k] = self.reverseSet(sList[i:i + k])
            else:
                toReverse = toReverse ^ 1
                continue
            toReverse = toReverse ^ 1
        
        print("".join(sList))
        return "".join(sList)
        
        
        
        
        
        