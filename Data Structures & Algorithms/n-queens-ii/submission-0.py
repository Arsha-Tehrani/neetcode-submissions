class Solution:
    def totalNQueens(self, n: int) -> int:
        #loop through top row and place queen in each slot.
            #after each queen placed alter the board with '#' to limit where you cant place a queen
            #feed that augmented board back in 
            #loop through top row, place queen, when hit with a # return and discard path
            #when n = 0, add to res


        res = 0
        board = [["." for _ in range(n)] for _ in range(n)]

        def dfs(i, plane):
            nonlocal res
            if i == 0:
                res += 1
                return

            for p in range(n):
                if plane[i-1][p] != '#':
                    temp = [row[:] for row in plane]
                    temp[i-1][p] = 'Q'
                    for row in range(len(plane)):
                        for col in range(len(plane[0])):
                            if row == i-1 and col == p:
                                continue
                            elif row == i-1:
                                temp[row][col] = '#'
                            elif col == p:
                                temp[row][col] = '#'
                            elif (row-(i-1)) == (col-p) or (row-(i-1)) == -(col-p):
                                temp[row][col] = '#'

                    dfs(i-1, temp)

                else:
                    continue

        dfs(n, board)

        return res
                            
                    
