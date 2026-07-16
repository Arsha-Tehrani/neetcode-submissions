class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        # i is the index in s, j is the index in t
        def dfs(i, j):
            # Base Cases
            if j == len(t): # We successfully matched all characters in t
                return 1
            if i == len(s): # We ran out of characters in s before matching t
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]

            # We can ALWAYS choose to skip the current character in s
            paths = dfs(i + 1, j)

            # If the characters match, we can ALSO choose to use this character
            if s[i] == t[j]:
                paths += dfs(i + 1, j + 1)

            # Cache the total number of paths from this state
            cache[(i, j)] = paths
            return paths

        # Start at index 0 for both strings
        return dfs(0, 0)