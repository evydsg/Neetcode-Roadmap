class Solution:
    def romanToInt(self, s: str) -> int:
        roman_rules = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        converted = 0
        indice = 0

        while indice < len(s):
            # Check for the subtraction case
            if indice + 1 < len(s) and roman_rules[s[indice]] < roman_rules[s[indice + 1]]:
                converted += roman_rules[s[indice + 1]] - roman_rules[s[indice]]
                indice += 2
            else:
                converted += roman_rules[s[indice]]
                indice += 1
        
        return converted


