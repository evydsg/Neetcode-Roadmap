class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        array_sum = sum(nums)
        left_sum = 0

        for index, num in enumerate(nums):
            right_sum = array_sum - left_sum - num

            if left_sum == right_sum:
                return index

            left_sum += num
        
        return -1