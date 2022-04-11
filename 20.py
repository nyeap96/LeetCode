#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
# 
#
#Example 1:
#
#Input: s = "()"
#Output: true
#Example 2:
#
#Input: s = "()[]{}"
#Output: true
#Example 3:
#
#Input: s = "(]"
#Output: false
# 
#
#Constraints:
#
#1 <= s.length <= 104
#s consists of parentheses only '()[]{}'.





class Solution:
    def isValid(self, s: str) -> bool:
        
        # i've done this problem before, but its a good problem. It demonstrates knoaledge and usage of the stack data structure
        # for this problem the solution is as follows:
        # if you see a left paren of any kind, you push onto a stack. And it you see a right paren of any kind you pop off the stack and see if it matches. This series of actions ensure that parens are matched even if they are nested
        
        
        myString = list(s)
        # in pyhton a list is same as stack, it even has pop function
        stack = [myString[0]]
        
        
        for i in range(1,len(myString)):
                        
            if myString[i] == ')':
                if not stack: return False
                top = stack.pop()
                if top != '(':
                    return False
                
            elif myString[i] == ']':
                if not stack: return False
                top = stack.pop()
                if top != '[':
                    return False
            
            elif myString[i] == '}':
                if not stack: return False
                top = stack.pop()
                if top != '{':
                    return False
            else:
                stack.append(myString[i])
        
        # this last one check for extraneous left parens
        if stack:
            return False
        return True
        
        