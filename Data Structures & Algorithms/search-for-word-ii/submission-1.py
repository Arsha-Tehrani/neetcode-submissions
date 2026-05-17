class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        res = []

        def add(word):
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            
            cur.end_word = True
        

        for i in words:
            add(i)

        def search(i, j, node, path):
            if node.end_word:
                res.append(path)
                node.end_word = False

            temp = board[i][j]
            board[i][j] = '#'

            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj

                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if board[ni][nj] in node.children:
                        search(ni, nj, node.children[board[ni][nj]], path + board[ni][nj])

            board[i][j] = temp

        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in self.root.children:
                    search(i,j,self.root.children[board[i][j]],board[i][j])

        return res