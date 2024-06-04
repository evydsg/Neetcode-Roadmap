class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dictionary = {}

        for character in s:
            if character in dictionary:
                return character
            
            dictionary[character] = 1
        
        return None
        