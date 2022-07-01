class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        myString = []
        
        for char in s:
            if char.isalnum():
                myString.append(char.lower())        
        
        #reverseString = list(reversed(myString))
        
        front = 0
        back = len(myString) - 1
        
        while front < back:
            if myString[front] != myString[back]:
                return False
            front += 1
            back -= 1
            
        return True
        
    
        