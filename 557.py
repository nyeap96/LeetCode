class Solution:
    def reverseWord(self,word):
        wordList = list(word)
        start = 0
        end = len(word) - 1
        while start < end:
            temp = wordList[start]
            wordList[start] = wordList[end]
            wordList[end] = temp
            start += 1
            end -= 1
        return "".join(wordList)
    def reverseWords(self, s: str) -> str:
        # ill split the array by white spaces into a list
        # then reverse each word individually
        # then join using white spaces again
        sList = s.split(' ')
        for i in range(0,len(sList)):
            sList[i] = self.reverseWord(sList[i])
        
        return ' '.join(sList)