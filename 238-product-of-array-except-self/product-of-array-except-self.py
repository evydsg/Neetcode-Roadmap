class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Array to append the results
        result = [0] * len(nums)

        prefix = 1

        #To calculate the product of each number 
        for index in range(len(nums)):
            result[index] = prefix
            prefix *= nums[index]

        postfix = 1

        #To reverse the array from back to start
        for index in range(len(nums)-1, -1, -1):
            result[index] *= postfix
            postfix *= nums[index]
        
        return result

        