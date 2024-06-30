class Solution:
    def isValid(self, s: str) -> bool:
        valid = []

        for character in s:
            if character == "]" or character ==  "}" or character == ")":
                if len(valid) == 0:
                    return False
                if character == "]" and valid[-1] == "[":
                    valid.pop()
                
                elif character == "}" and valid[-1] == "{":
                    valid.pop()
                
                elif character == ")" and valid[-1] == "(":
                    valid.pop()
                else:
                    return False
            else:
                valid.append(character)

            
        if len(valid) == 0:
            return True
        
        return False

        