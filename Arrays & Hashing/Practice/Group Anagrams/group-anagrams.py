from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Understand:
            - The idea is to find the strings that are anagrams and return them as a list

            Questions:
                - Can we have any other character than letters?
                - Are we always guaranteed to have lowercase letters?
                - Are we always guaranteed to have anagrams?

        Match:
            - Use dictionaries to keep track of the anagrams

        Plan:
            - Initialize a dictionary
            - Traverse through the list
            - Sort the word (key)
            - Check if the key is the dictionary
                - Yes, we append the word to the key
                - No, we add the word and the key to the dictionary
        """
        dictionary = {}

        for word in strs:
            word_sorted = ''.join(sorted(word))

            if word_sorted in dictionary:
                dictionary[word_sorted].append(word)
            else:
                dictionary[word_sorted] = [word]

        return dictionary.values()
