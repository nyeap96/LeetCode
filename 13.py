#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.
#
# 
#
#Example 1:
#
#Input: s = "III"
#Output: 3
#Explanation: III = 3.
#Example 2:
#
#Input: s = "LVIII"
#Output: 58
#Explanation: L = 50, V= 5, III = 3.
#Example 3:
#
#Input: s = "MCMXCIV"
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#
#Constraints:
#
#1 <= s.length <= 15
#s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#It is guaranteed that s is a valid roman numeral in the range [1, 3999].




class Solution:
    def romanToInt(self, s: str) -> int:
        
        # so here we wanna do simply addition, but we can add in special cases for the 6 subtraction instances
        # in fact, i dont think we even need to do subtraction there, we can just add less based on the previous value
        
        
        myDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000            
        }
        
        result = 0
        # now we just do the first value, no matter what it is we can just add whatever because instead of subtraction we are doing an add less because the next value is always going to add, it could just add more or add less based on previous value
        myString = list(s)
        result += myDict[myString[0]]
        
        for i in range(1,len(myString)):
            
            if myString[i] == 'V' and myString[i - 1] == 'I':
                result += 3
            elif myString[i] == 'X' and myString[i - 1] == 'I':
                result += 8
            elif myString[i] == 'L' and myString[i - 1] == 'X':
                result += 30
            elif myString[i] == 'C' and myString[i - 1] == 'X':
                result += 80
            elif myString[i] == 'D' and myString[i - 1] == 'C':
                result += 300
            elif myString[i] == 'M' and myString[i - 1] == 'C':
                result += 800
            else:
                result += myDict[myString[i]]
        return result
                
            
            
            
        
        