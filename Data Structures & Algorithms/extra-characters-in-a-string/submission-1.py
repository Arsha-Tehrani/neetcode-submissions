class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordSet = set(dictionary)
        memo = {}

        def dfs(start_i: int) -> int:
            if start_i == len(s):
                return 0
            if start_i in memo:
                return memo[start_i]

            # Choice 1: Skip s[start_i] as an extra character (+1)
            res = 1 + dfs(start_i + 1)

            # Choice 2: Try matching any dictionary word starting at start_i (+0)
            cur = ""
            for ind in range(start_i, len(s)):
                cur += s[ind]
                if cur in wordSet:
                    res = min(res, dfs(ind + 1))

            memo[start_i] = res
            return res

        return dfs(0)