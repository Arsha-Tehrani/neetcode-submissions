class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for cell in range(len(grid[0])):
                if grid[row][cell] == 1:
                    res += 4
                    if row > 0 and grid[row-1][cell] == 1:
                        res -= 1
                    if row < len(grid)-1 and grid[row+1][cell] == 1:
                        res -= 1
                    if cell > 0 and grid[row][cell-1] == 1:
                        res -= 1
                    if cell < len(grid[0])-1 and grid[row][cell+1] == 1:
                        res -= 1

        return res 