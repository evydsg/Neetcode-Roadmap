class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        
        stack = []
        
        for token in tokens:

                if token == "+":
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operand1 + operand2
                    stack.append(result)

                elif token == "-":
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operand1 - operand2
                    stack.append(result)
                    
                elif token == "*":
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operand1 * operand2
                    stack.append(result)
            
                elif token == "/":
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = int(operand1/ operand2)
                    stack.append(result)
                
                else:
                    stack.append(int(token))
            
        return stack.pop()
    
    """
    Understand:
                - can the string be empty?
                - can we have only operands?
                - can we have negative numbers?
    Match:
                - Stacks
    Plan:       
                1. Check if list is empty, if so, return 0
                2. Traverse through the list
                3. If the token is an operand, we insert in the stack 
                4. Check what is the operator
    """
