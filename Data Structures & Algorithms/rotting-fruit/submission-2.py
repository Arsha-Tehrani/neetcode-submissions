class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        points = []
        mins = 0
        fruits = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fruits = True
                if grid[i][j] == 2:
                    points.append((i,j))

        if not fruits:
            return 0

        while len(points) > 0:
            mins += 1
            print(grid)
            length = len(points)
            for i in range(length):
                cur = points.pop(0)
                row = cur[0]
                col = cur[1]

                if row > 0 and grid[row-1][col] == 1:
                    grid[row-1][col] = 2
                    points.append((row-1, col))
                if col > 0 and grid[row][col-1] == 1:
                    grid[row][col-1] = 2
                    points.append((row, col-1))
                if row < len(grid) - 1 and grid[row+1][col] == 1:
                    grid[row+1][col] = 2
                    points.append((row+1, col))
                if col < len(grid[row]) - 1 and grid[row][col+1] == 1:
                    grid[row][col+1] = 2
                    points.append((row, col+1))

        if mins == 0:
            return -1
        
        for i in grid:
            for j in i:
                if j == 1:
                    return -1

        return mins-1
        


                