class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        if n == 0:
            return 1
    
        for i in range(1, abs(n)):
            res *= x

        if n > 0:
            return res
        
        return 1/res