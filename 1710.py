class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # so this problem is essentially just a sorting problem
        # you sort buy priority of boxes because some boxes all take up the same space and have more units
        # so some boxes are just better than other boxes based on how many units are in each box
        # so sort by numver of units and taek from the front as much as possible
        
        
        myList = sorted(boxTypes, key=lambda x: (x[1]))
        print(myList)
        
        cursor = len(myList) - 1
        numBoxes = 0
        
        print(myList[cursor])
        
        while truckSize > 0:
            
            if cursor < 0:
                break
            
            if truckSize - myList[cursor][0] >= 0:
                numBoxes += myList[cursor][0] * myList[cursor][1];
                truckSize -= myList[cursor][0]
            
            else:
                while truckSize > 0:
                    numBoxes += myList[cursor][1]
                    truckSize -= 1
            
            if truckSize <= 0:
                break
            
            cursor -= 1
            
        return numBoxes
            
            