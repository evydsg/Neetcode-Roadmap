class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        answer = []*k

        for number in nums:
            if number in dictionary:
                dictionary[number] += 1

            else:
                dictionary[number] = 1
        
        sorted_dictionary = sorted(dictionary.items(), key = lambda item: item[1], reverse = True)

        answer = [item[0] for item in sorted_dictionary[:k]]
        return answer