class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {} #To keep track of how many times the integers appears

        for number in nums: #Go through every number in nums
            if number in dictionary: #If the number already exists in the dictionary, we return true
                return True

            dictionary[number] = 1 #If the number does not exist in dictionary, we add to the dictionary

        return False