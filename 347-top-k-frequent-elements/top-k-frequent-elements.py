class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        if len(nums) == k:
            return list(nums)

        dictionary = {}
        answer = []
        
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        dictionary_sorted = sorted(dictionary.items(), key=lambda x: x[1], reverse = True)
        for item in dictionary_sorted[:k]:
            answer.append(item[0])

        return answer
        