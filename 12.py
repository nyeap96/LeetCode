class Solution:
    def intToRoman(self, num: int) -> str:
        # okay so i think this can be done by extracting the values and then putting in the corresponding roman numberal values
        # also the number is only between 1 and 3999 so we can kinda brute ofrce process each portion
        # so lets start by extracting values from the back of our decimal number
        roman = ['I','V','X','L','C','D','M']
        romanIndex = 0
        res = ""
        while num > 0:
            rem = num % 10
            if rem == 4:
                res = roman[romanIndex] + roman[romanIndex + 1] + res
            elif rem == 9:
                res = roman[romanIndex] + roman[romanIndex + 2] + res
            else:
                if rem > 4:
                    rem -= 5
                    res = roman[romanIndex + 1] + (roman[romanIndex] * rem) + res
                else:
                    res = (roman[romanIndex] * rem) + res
            num = num // 10
            romanIndex += 2 
        
        return res
        