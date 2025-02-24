class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(heap)

        while k > 0:
            frequency, num = heapq.heappop(heap)
            result.append(num)
            k -= 1
        
        return result