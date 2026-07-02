class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1

        def dfs(row, col, res):
            if row >= m or col >= n:
                return 0

            if dp[row][col]:
                res += dp[row][col]
                return res

            dp[row][col] = dfs(row+1, col, 0) + dfs(row, col+1, 0)
            return dp[row][col]

        return dfs(0, 0, 0)
        