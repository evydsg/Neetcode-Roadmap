class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        prefix_sum = {0:1}
        result = 0

        for num in nums:
            current_sum += num

            difference = current_sum - k
            if difference in prefix_sum:
                result += prefix_sum[difference]
            
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1
        
        return result