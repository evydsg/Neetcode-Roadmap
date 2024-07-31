class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Understand:
            - The idea is to check if the two strings have the same number of letters 

            Questions:
                - Are we always guaranteed to get a string with lower case letters?
                - Can we have any other character than letters?

        Match:
            - Use dictionary to keep track of how many times a character appears

        Plan:
            - Initialize dictionaries for both strings
            - Traverse through the strings and add them to the dictionary, as well as the counter
            - Compare if both dictionaries are the same
        """
        dictionary_s = {}
        dictionary_t = {}

        if len(s) != len(t):
            return False

        for character in s:
            if character in dictionary_s:
                dictionary_s[character] += 1
            else:
                dictionary_s[character] = 1

        for character in t:
            if character in dictionary_t:
                dictionary_t[character] += 1
            else:
                dictionary_t[character] = 1

        if dictionary_s != dictionary_t:
            return False

        return True

        
