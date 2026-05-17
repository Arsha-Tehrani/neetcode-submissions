class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        len_row = len(board)
        len_col = len(board[0])

        for i in range(len_row):
            row = {}
            col = {}
            for j in range(len_col):
                if board[i][j] != ".":
                    row[board[i][j]] = row.get(board[i][j], 0) + 1
                    if row[board[i][j]] >= 2:
                        return False

                if board[j][i] != ".":
                    col[board[j][i]] = col.get(board[j][i], 0) + 1
                    if col[board[j][i]] >= 2:
                        return False


        def checkbox(board, i, j):
            # check this 3×3 box
            box = {}
            for r in range(3):
                for c in range(3):
                    slot = board[i + r][j + c]
                    if slot != ".":
                        box[slot] = box.get(slot, 0) + 1
                        if box[slot] > 1:
                            return False

            # move to next box (recursion)
            # next column
            if j + 3 < 9:
                return checkbox(board, i, j + 3)

            # next row of boxes
            if i + 3 < 9:
                return checkbox(board, i + 3, 0)

            # no more boxes
            return True

        # start recursion at top-left 3×3 box
        return checkbox(board, 0, 0)