class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        if len(s) != len(t):
            return False
  
        for character in s:
            if character in count_s:
                count_s[character] += 1
            else:
                count_s[character] = 1
        
        for character in t:
            if character in count_t:
                count_t[character] += 1
            else:
                count_t[character] = 1
        
        if count_s == count_t:
            return True
        

        return False  