class Solution:
    def canWinNim(self, n: int) -> bool:
        # commonly heard of game
        # the strat is essentially to set it up so that no matter what you take the n-4 stone
        # here you and friend can take 1-3 stones
        # this means that optimally when there are 5 stones left then a winner is determined
        # but you simply extend this all the way to the beginning of the game
        # this means that once you know the value n and who goes first, then the outcome is predetermined
        # in this case, since everyone plays optimally, only 4 stones are taken per turn because everyone does the optimal move to try to get last stone
        # this can be proben by the following. once you start, you want the opponent get the n-4 stone
        # this is guaranteed by making your firedn get the n-8 stone
        # so for n = 1-3 its true because i go first and get all the stones
        # for n = 4 i go first and no matter what what i lose
        # i take one stone, friend takes three i lose
        # i take three stones, firend take one i lose
        # for n=5 i win because i take only one stone, friend and firend has to take n-4 stone so i win
        # for n=6 same situation because i take 3 stones
        # for n=7 i take 3 and win
        # for n=8 i lose because i take 1 then friend takes 3 and i have to take fourth stone and lose
        # so it looks like every fourth stone the winner changes
        # do the formulat should look like every fourth stone my friend wins otherwise i win
        
        return n % 4
         
        
        
        
        