class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #row, col, val
        cache = {}
        res = 0
        def dfs(i, j):
            up, down, left, right = 0, 0, 0, 0

            if (i,j) in cache:
                return cache[(i,j)]

            if i < len(matrix) - 1 and matrix[i+1][j] > matrix[i][j]:
                down = dfs(i+1, j)

            if j < len(matrix[0]) - 1 and matrix[i][j+1] > matrix[i][j]:
                right = dfs(i, j+1)

            if i > 0 and matrix[i-1][j] > matrix[i][j]:
                up = dfs(i-1, j)

            if j > 0 and matrix[i][j-1] > matrix[i][j]:
                left = dfs(i, j-1)

            cache[(i,j)] = max(up, down, right, left) + 1
            
            return cache[(i,j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cur = dfs(i, j)
                res = max(cur, res)

        return res

            