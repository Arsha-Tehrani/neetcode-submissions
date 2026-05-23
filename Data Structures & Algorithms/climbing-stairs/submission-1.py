class Solution:
    def climbStairs(self, n: int) -> int:
        total = {}

        def dfs(step):
            if step in total:
                return total[step]

            if step == n:
                return 1
            if step > n:
                return 0

            way = dfs(step+1) + dfs(step+2)
            total[step] = way

            return way

        return dfs(0)