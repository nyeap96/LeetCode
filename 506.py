import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        #so i think you can do this is n time
        # you can make a copy of the list and heapify it in 2n time
        # then insert the heap into a dictionary which is also n
        # then iterate over score while building the result array which is another 2n
        
        # so first you make a copy and heapify
        # oh but need to make negative for max heap cause python only does min heap
        # or at the point where i try to assign numbers i change that process so i can keep things kinda the same instead of doinga  bunch of multiplying by -1
        heap = score.copy()
        heapq.heapify(heap)
        
        
        # now put into a dictionary
        scorePlace = {}
        
        i = len(score)
        while heap:
            temp = heapq.heappop(heap)
            scorePlace[temp] = i
            i -= 1
        # ok now intialize a result array and put the corresponding values in
        print(score)
        
        res = []
        for i in range(0,len(score)):
            if scorePlace[score[i]] > 3:
                res.append(str(scorePlace[score[i]]))
            else:
                if scorePlace[score[i]] == 1:
                    res.append("Gold Medal")
                elif scorePlace[score[i]] == 2:
                    res.append("Silver Medal")
                else:
                    res.append("Bronze Medal")
        return res
        
        
        