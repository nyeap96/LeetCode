class Solution:
    def checkRow(self,firstChar,row1,row2,row3):
        if firstChar in row1:
            return 1
        elif firstChar in row2:
            return 2
        else:
            return 3
    
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q','w','e','r','t','y','u','i','o','p'}
        row2 = {'a','s','d','f','g','h','j','k','l'}
        row3 = {'z','x','c','v','b','n','m'}
        
        res = []
        
        for word in words:
            row = self.checkRow(word[0].lower(),row1,row2,row3)
            i = 1
            while i < len(word):
                if row == 1:
                    if word[i].lower() not in row1:
                        break
                if row == 2:
                    if word[i].lower() not in row2:
                        break
                if row == 3:
                    if word[i].lower() not in row3:
                        break
                i += 1
            if i == len(word):
                res.append(word)
        return res
                
            