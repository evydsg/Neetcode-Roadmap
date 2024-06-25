class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        index = 0
        nums.sort()

        for index in range(len(nums)-2):
            if nums[index] > 0:
                break
            
            if index > 0 and nums[index] == nums[index-1]:
                continue

            left = index + 1
            right = len(nums)-1

            while left < right:
                Sum = nums[index] + nums[left] + nums[right]
                array = [nums[index], nums[left], nums[right]]

                if Sum < 0:
                    left += 1
                elif Sum > 0:
                    right -= 1

                else:
                    answer.append(array)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates

                    left += 1
                    right -=1
        return answer