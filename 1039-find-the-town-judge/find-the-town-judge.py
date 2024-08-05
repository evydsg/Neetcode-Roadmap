class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 0:
            return -1
        
        # Initialize two arrays to keep track of trust relationships
        trust_counts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)
        
        # Populate the trust arrays
        for a, b in trust:
            trust_counts[a] += 1
            trusted_by[b] += 1
        
        # Identify the judge
        for i in range(1, n + 1):
            if trust_counts[i] == 0 and trusted_by[i] == n - 1:
                return i
        
        return -1


