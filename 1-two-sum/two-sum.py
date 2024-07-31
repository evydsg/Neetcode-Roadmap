class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
            Understand:
                - The idea is to find two numbers that can add up together to the target

                Questions:
                    - Are we always guaranteed to have an answer?
                    - Are we always guaranteed to positive integers?
                    - Can we have an empty list?
            
            Match:
                - Dictionary that keeps track of the current number and difference between him
            
            Plan:
                - Initialize a dictionary
                - Traverse through the list calculating the difference and the target
                - Check if the difference exists in the dictionary

            Evaluate:
                - 

        """
        dictionary = {}

        for indice in range(len(nums)):
            difference = target - nums[indice]

            if difference in dictionary:
                return [dictionary[difference], indice]
            
            dictionary[nums[indice]] = indice