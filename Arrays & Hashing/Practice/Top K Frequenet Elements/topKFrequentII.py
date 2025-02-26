class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        count = {}
        frequency =[[] for index in range(len(nums) + 1)]

        for number in nums:
            count[number] += 1 + count.get(number, 0)

        for number, freq in count.items():
            frequency[freq].append(number)
        
        result = []

        for index in range(len(nums)-1, 0, -1):
            for number in frequency[index]:
                result.append(number)

                if len(result) == k:
                    return result