class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        stack = []
        INF = 2147483647
        def bfs(row, col):
            while len(stack) > 0:
                for i in range(len(stack)):
                    cur = stack.pop(0)
                    row = cur[0]
                    col = cur[1]
                    val = cur[2]
                    grid[row][col] = min(val + 1, grid[row][col])

                    if row > 0 and grid[row-1][col] > val+2:
                        stack.append((row-1, col, val+1))
                    
                    if col > 0 and grid[row][col-1] > val+2:
                        stack.append((row, col-1, val+1))

                    if row < len(grid)-1 and grid[row+1][col] > val+2:
                        stack.append((row+1, col, val+1))
                    
                    if col < len(grid[0])-1 and grid[row][col+1] > val+2:
                        stack.append((row, col+1, val+1))

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    if row > 0 and grid[row-1][col] != -1:
                        stack.append((row-1, col, 0))
                    
                    if col > 0 and grid[row][col-1] != -1:
                        stack.append((row, col-1, 0))

                    if row < len(grid)-1 and grid[row+1][col] != -1:
                        stack.append((row+1, col, 0))
                    
                    if col < len(grid[0])-1 and grid[row][col+1] != -1:
                        stack.append((row, col+1, 0))
                bfs(row, col)
                

