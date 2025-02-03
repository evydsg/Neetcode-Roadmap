class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0

        for number in nums:
            total += number
            self.prefix.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        rightRange = self.prefix[right]
        leftRange = self.prefix[left - 1] if left > 0 else 0

        return rightRange - leftRange