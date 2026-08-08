class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
        #Representation of 16 - 0
        '''10000
        1111
        1110
        1101
        1100
        1011
        1010
        1001
        1000
        111
        110
        101
        100
        11
        10
        0'''