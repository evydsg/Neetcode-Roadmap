def removeDuplicatesII(self, nums: List[int]) -> int:
    left, right = 0, 0

    while right < len(nums)-1:
        count = 1
        while nums[right] == nums[right + 1]:
            right += 1
            count += 1
        
        for index in range(min(2, count)):
            nums[left] = nums[right]
            left += 1
        
        right += 1
    
    return left