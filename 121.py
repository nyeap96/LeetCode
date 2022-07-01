class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # right so the key here is about findg out when the aray goes from ascending to not
        # when the array goes from ascending to not it is a local maximum and a point of profit
        # record all of those and find the max to get the answer
        # we'll do a two pointer approach here
        # pointer one will point to a local min
        # second pointer wil traverse array and find local maxima
        
        if not prices:
            return 0
        
        start = 0
        end = 1
        maxPrice = 0
        
        
        while end < len(prices):
            maxPrice = max(maxPrice, prices[end] - prices[start])
            if prices[end] < prices[start]:
                start = end
            end += 1
        return maxPrice
            
            
            
            
            
            
            
            
            
            
            