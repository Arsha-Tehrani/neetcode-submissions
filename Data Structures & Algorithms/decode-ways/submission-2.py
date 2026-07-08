class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[len(s)] = 1
        end = len(s)-1
        temp = int(s[end])
        if temp > 0 and temp < 27:
            dp[end] = 1
        
        for i in range(len(s)-2, -1, -1):
            cur = s[i]
            cur_int = int(cur)

            if cur_int > 0:
                temp = int(cur + s[i+1])
                dp[i] = dp[i+1]

                if temp > 0 and temp < 27:
                    dp[i] += dp[i+2]

        
        return dp[0]
                

        