class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [""]
        
        dictionary = {}
        
        for word in strs:
            new_word = word.lower()
            word_sorted = ''.join(sorted(new_word)) 
            
            if word_sorted in dictionary:
                dictionary[word_sorted].append(new_word)
            else:
                dictionary[word_sorted] = [new_word]
        
        return list(dictionary.values())
