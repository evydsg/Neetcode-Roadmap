class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * (len(temperatures))
        
        # Iterate through each index in temperatures
        for index in range(len(temperatures)):
            # While stack is not empty and current temperature is warmer than temperature at stack's top
            while stack and temperatures[index] > temperatures[stack[-1]] :
                top = stack.pop()
                result[top] = index - top
            # Push current index onto stack
            stack.append(index)
    
        
        return result
