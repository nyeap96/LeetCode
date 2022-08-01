class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # hm okay so you want to give as many children a cookie that is bigger or equal to their greed factor
        # so one thing is that this is about the realtionship between the size of cookies and greed factor
        # so for the first example the cookies are only of size 1 so any child with greed factor above 1 cannot be satisfied
        # so maybe what you can do is a sort of greedy algorithm
        # simply match big cookies to big children if possible
        # are the cookies and children sorted?
        # if so you could just like go the the first child that has a greed factor satisfiable by the biggest cookie and start iterating backwards down both lists of sorts
        # im thinking greedy algorithm is best
        # start by sorting both, then starting with cookies go down until you can stisfy then go down both lists
        
        g.sort()
        s.sort()
        
        cookies = len(s) - 1
        children = len(g) - 1
        res = 0
        while cookies >= 0 and children >= 0:
            if s[cookies] >= g[children]:
                res += 1
                cookies -= 1
                children -= 1
            elif s[cookies] < g[children]:
                children -= 1
        return res
        
        
        
        
        
        
        
        
        