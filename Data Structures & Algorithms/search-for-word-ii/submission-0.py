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

        def search(i, j, root, char):
            if root.end_word: 
                res.append(char) 
                root.end_word = False

            visited = board[i][j]
            board[i][j] = '#'
            
            if i > 0: 
                if board[i-1][j] in root.children: 
                    temp = char + board[i-1][j] 
                    search(i-1, j, root.children[board[i-1][j]], temp) 
                    
            if i < len(board)-1: 
                temp = char + board[i+1][j] 
                if board[i+1][j] in root.children: 
                    search(i+1, j, root.children[board[i+1][j]], temp) 
                    
            if j > 0: 
                temp = char + board[i][j-1] 
                if board[i][j-1] in root.children: 
                    search(i, j-1, root.children[board[i][j-1]], temp) 
            
            if j < len(board[0])-1: 
                temp = char + board[i][j+1]
                if board[i][j+1] in root.children: 
                    search(i, j+1, root.children[board[i][j+1]], temp) 

            board[i][j] = visited
            
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in self.root.children:
                    search(i,j,self.root.children[board[i][j]],board[i][j])

        return res