class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_length = 0
        
        for num in hashset:
            if num - 1 not in hashset:
                count = 1
                current_num = num

                while (current_num + 1) in hashset:
                    current_num +=1 
                    count +=1
            
                max_length = max(max_length, count)

        return max_length