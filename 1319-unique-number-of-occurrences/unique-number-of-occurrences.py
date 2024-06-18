class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        U-nderstand:
                    - Can we have an empty list?
                    - 
        M-atch:
                    - Hashmap to keep track of ocurrences
                    - Compare each key[value] to see if they are different
        Plan:
                    - Traverse through the list
                    - Keep track of #of occurrences
        """
        dictionary = {}
        for num in arr:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        lst = list(dictionary.values())
        setDictionary = set(lst)
    

        if len(lst) == len(setDictionary):
            return True
        
        return False
        
