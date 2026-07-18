class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                result = i == len(s)
            else:
                first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

                if j + 1 < len(p) and p[j + 1] == '*':
                    # zero occurrences, OR one+ occurrences (consume s[i], stay on same p[j])
                    result = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
                else:
                    result = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)