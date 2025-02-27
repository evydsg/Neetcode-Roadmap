class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for word in strs:
            string += str(len(word)) + "!" + word
        
        return string

    def decode(self, s: str) -> List[str]:
        list_strings = []
        index = 0

        while index < len(s):
            second = index
            
            while s[second] != "!":
                second += 1
            
            length = int(s[index : second])
            word = s[second + 1: second + length + 1]
            index = length + second + 1

            list_strings.append(word)
    
        return list_strings