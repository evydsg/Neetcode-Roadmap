class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(character for character in s if character.isalnum())

        if len(s) == 0:
            return True

        left, right = 0, len(s)-1

        while left <= right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -=1

        return True