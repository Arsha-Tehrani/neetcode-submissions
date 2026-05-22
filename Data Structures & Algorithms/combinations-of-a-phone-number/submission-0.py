class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        board = [ #numbers from 0 - 7 = 2 - 9
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i'],
            ['j','k','l'],
            ['m','n','o'],
            ['p','q','r','s'],
            ['t','u','v'],
            ['w','x','y','z']
        ]

        def dfs(i, cur):
            #print(cur)
            #print(i)
            if len(cur) == len(digits):
                result = "".join(cur)
                res.append(result)
                return
            
            if len(cur) > len(digits):
                return 


            #add something from first num ()
            #call function looking for something from second num
            #traceback
            #add next one from first num
            if i < len(digits):
                a = int(digits[i])-2
                for p in range(len(board[a])):
                    cur.append(board[a][p])
                    dfs(i+1, cur)
                    cur.pop()

        dfs(0, [])
        
        if res[0] == "":
            return []
        
        return res


