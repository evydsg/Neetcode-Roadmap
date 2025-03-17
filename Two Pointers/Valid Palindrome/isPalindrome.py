class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char.lower() for char in s if char.isalnum())
        print(string)
        left, right = 0, len(string)-1

        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1 
        
        return True