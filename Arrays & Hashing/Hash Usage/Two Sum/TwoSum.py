class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_hash = {}

        for index, num in enumerate(nums):
            difference = target - num

            if difference in prev_hash:
                return [prev_hash[difference], index]
            else:
                prev_hash[num] = index