class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        setNums = set(nums)
        maxL = 0

        for num in nums:
            if num-1 not in setNums:
                temporaryNum = num
                length = 1

                while temporaryNum + 1 in setNums:
                    length += 1 
                    temporaryNum = temporaryNum + 1
                
                maxL = max(length, maxL)

        return maxL