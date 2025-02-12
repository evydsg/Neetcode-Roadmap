from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_array = []
        postfix_array = []
        output_array = [1] * len(nums)  # Fix incorrect initialization

        # Prefix Product Calculation
        for num in nums:
            prefix_array.append(prefix)
            prefix *= num

        # Postfix Product Calculation
        postfix = 1
        for index in range(len(nums) - 1, -1, -1):
            postfix_array.append(postfix)
            postfix *= nums[index]

        # Reverse postfix_array to align with prefix_array
        postfix_array.reverse()

        # Compute Final Output Array
        for index in range(len(nums)):
            output_array[index] = prefix_array[index] * postfix_array[index]

        return output_array



        
        
        