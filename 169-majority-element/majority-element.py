class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        maxCount = 0
        value = None

        for number in nums:
            if number not in dictionary:
                dictionary[number] = 1
            
            else:
                dictionary[number] += 1
        
        for key, count in dictionary.items():
            if count > maxCount:
                maxCount = count
                value = key
        
        return value
            

