class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        target = list(word)

        def dfs(i, j, cur, visited):
            cur.append(board[i][j])
            cord = (i,j)
            visited[cord] = 1

            if cur == target:
                return True

            if i+1 < len(board) and visited.get((i+1, j), 0) == 0:
                if dfs(i+1, j, cur, visited): return True

            if j+1 < len(board[0]) and visited.get((i, j+1), 0) == 0:
                if dfs(i, j+1, cur, visited): return True

            if i-1 >= 0 and visited.get((i-1, j), 0) == 0:
                if dfs(i-1, j, cur, visited): return True

            if j-1 >= 0 and visited.get((i, j-1), 0) == 0:
                if dfs(i, j-1, cur, visited): return True

            cur.pop()
            visited[cord] = 0
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, [], {}):
                    return True
        
        return False
            


            