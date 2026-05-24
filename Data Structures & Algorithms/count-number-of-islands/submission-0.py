class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #LOOP THROUGH ISLAND
        #when hit land:
            #call helper 
        total = 0

        def helper(row, col):
            if grid[row][col] == '1':
                grid[row][col] = "0"
                if row < len(grid)-1:
                    helper(row+1, col)
                if row > 0:
                    helper(row-1, col)
                if col < len(grid[0])-1:
                    helper(row, col+1)
                if col > 0:
                    helper(row,col-1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    helper(row, col)
                    total += 1

        return total

