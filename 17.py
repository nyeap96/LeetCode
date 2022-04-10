#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# 
#
#Example 1:
#
#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#Example 2:
#
#Input: digits = ""
#Output: []
#Example 3:
#
#Input: digits = "2"
#Output: ["a","b","c"]
# 
#
#Constraints:
#
#0 <= digits.length <= 4
#digits[i] is a digit in the range ['2', '9'].


# i definitely need more practice for recursion problems this took a lot of looking at other solutions to figure out
class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        # so this seems like a recursion problem. 
        
        # first start with just one digit
        
        myDict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        # recursion always has a base case, here the base case would be just haveing zero digits
        
        results = []
        
        def recurse(reducedDigits,permutation):
            if len(reducedDigits) == 0:
                results.append(permutation)
                print(results)
                return
            # for each letter in my dictionary so for first call letter = 'a' and then it resurses but without the 2 in '23' 
            # then it looks up '3' and adds 'd' to the string on first call
            # it hits base case, adds to essentially global variable
            # then goes returns back into this loop and adds 'e'
            for letter in myDict[reducedDigits[0]]:
                recurse(reducedDigits[1:],permutation + letter)
        
        
        recurse(digits,'')
        return results
        
        
        
        
        
        
        