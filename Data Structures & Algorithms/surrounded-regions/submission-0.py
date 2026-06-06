class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #Get region coordinates with dFS
        #change all the stuff to X

        visited = set()
        fail = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] == "X" or (row, col) in visited:
                return 
            
            visited.add((row, col))
            if row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1:
                visited.add(-1)
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in fail:
                    dfs(row, col)

                    if -1 in visited:
                        fail = visited.copy()
                        visited.clear()

                    for node in visited:
                        r = node[0]
                        c = node[1]
                        board[r][c] = "X"
                    visited.clear()


