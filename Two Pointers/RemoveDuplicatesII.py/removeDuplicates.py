class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        checkDuplicates = {}
        k = 0

        for index in range(len(nums)):
            if nums[index] in checkDuplicates:
                checkDuplicates[nums[index]] += 1

                if checkDuplicates[nums[index]] <= 2:
                    nums[k] = nums[index]
                    k += 1
            else:
                nums[k] = nums[index]
                k += 1
                checkDuplicates[nums[index]] = 1
        
        return k
