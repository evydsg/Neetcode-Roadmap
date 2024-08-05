class Solution:
    def fib(self, n: int) -> int:
        res = 0
        if n <=1:
            return n
    
        return self.fib( n - 1) + self.fib(n - 2)
    
        