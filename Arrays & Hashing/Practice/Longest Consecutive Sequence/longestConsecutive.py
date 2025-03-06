class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0

        for num in nums_set:
            count = 0

            if num - 1 not in nums_set:
                count += 1

                while num + 1 in nums_set:
                    num = num + 1
                    count += 1
            
            if result < count:
                result = count
        
        return result

