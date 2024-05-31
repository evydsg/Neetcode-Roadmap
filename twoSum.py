class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} #To keep track of the integers and their own indices
        index = 0 #To loop through the array

        for index in range(len(nums)):
            difference = target - nums[index]

            if difference in dictionary:
                return [dictionary[difference], index]
            
            dictionary[nums[index]] = index