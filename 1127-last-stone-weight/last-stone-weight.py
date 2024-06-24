class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 0:
            stones.sort()

            largest1 = stones[-1]
            largest2 = stones[-2]

            if largest1 > largest2:
                stones.remove(largest1)
                stones.remove(largest2)
                stones.append(largest1 - largest2)
            
            elif largest1 == largest2:
                stones.remove(largest1)
                stones.remove(largest2)
            
            if len(stones) == 1:
                return stones[0]
        
        return 0