class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bredth first search, but for each 
        #one make it depth as well but alter the grid when a node is impossible

        ROWS = len(heights)
        COLUMNS = len(heights[0])
        res = []

        pac_vis, atl_vis = set(), set()

        def dfs(row, col, visited, val):
            if (row, col) in visited or row < 0 or col < 0 or row == ROWS or col == COLUMNS or heights[row][col] < val:
                return
            visited.add((row, col))

            dfs(row-1, col, visited, heights[row][col])
            dfs(row+1, col, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])

        for c in range(COLUMNS):
            dfs(0, c, pac_vis, 0)
            dfs(ROWS-1, c, atl_vis, 0)

        for r in range(ROWS):
            dfs(r, 0, pac_vis, 0)
            dfs(r, COLUMNS-1, atl_vis, 0)

        for node in pac_vis:
            if node in atl_vis:
                res.append(node)

        return res

            