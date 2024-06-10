class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = [] #To store the answer
        nums.sort() #To sort the array, so that we don't have duplicates in the answer

        for index, value in enumerate(nums): #index = index of the current value, value = value at index 
            if index > 0 and value == nums[index - 1]: #In case it is not the first value and it is the same as the previous value
                continue
            
            left, right = index + 1, len(nums) - 1 #Two Sum II approach using two pointers
            
            while left < right:
                threeSum = value + nums[right] + nums[left]

                if threeSum >  0: #Decrement right pointer
                    right -= 1
                elif threeSum < 0: #Increment left pointer
                    left += 1
                else:
                    answer.append([value, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left-1] and left < right: #Check if the values are the same
                        left +=1
        return answer