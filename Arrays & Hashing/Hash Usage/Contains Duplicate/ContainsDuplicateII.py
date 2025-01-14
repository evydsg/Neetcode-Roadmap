class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictNums = {}

        for num in nums:
            if num in dictNums:
                return True
            else:
                dictNums[num] = 1
        
        return False