class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k, index = 0, 0

        for index in range(len(nums)-1):
            if nums[index] != nums[index+1]:
                number = nums[index]
                nums[k] = number
                k+=1
        
        nums[k] = nums[-1]
        k +=1
        
        return k