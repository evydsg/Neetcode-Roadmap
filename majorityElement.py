class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}

        for number in nums:

            if number in dictionary: 
                dictionary[number] += 1

            else:
                dictionary[number] = 1
            
            if dictionary[number] > (len(nums)/2):
                return number

        return 1