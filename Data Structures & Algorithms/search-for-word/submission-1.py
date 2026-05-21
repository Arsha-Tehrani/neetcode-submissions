class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        target = list(word)

        def dfs(i, j, index):

            if index == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            res = dfs(i+1, j, index+1) or dfs(i-1, j, index+1) or dfs(i, j+1, index+1) or dfs(i, j-1, index+1)

            board[i][j] = temp

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False

        


            