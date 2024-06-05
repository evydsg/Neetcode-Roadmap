class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        string = ''.join([char for char in string if "a" <=char <= 'z' or ('0' <= char <= '9')])
        left, right = 0, len(string)-1

        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True