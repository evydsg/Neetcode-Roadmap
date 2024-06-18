class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        if len(s) == 0:
            return t

        dictionary = {}

        for character in t:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
        
        for character in s:
            if character in dictionary:
                dictionary[character] -= 1
            else:
                dictionary[character] = 1

        
        for key in dictionary:
            if dictionary[key] == 1:
                return key
            

        