class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1

        #Prefix Product
        for index, num in enumerate(nums):
            prefix *= num
            nums[index] = prefix
        
        postfix = 1
        for index in range(len(nums)-1, -1, -1):
            postfix *= nums[index] if index < len(nums)-1 else 1
            nums[index] *= postfix
        
        
        