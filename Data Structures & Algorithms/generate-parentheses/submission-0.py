class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #have a counter i to track how many character you have used. 
        #every loop one runs with a close added and one with open added
        # if i hits 2*n then you stop.
        #check if valid pair

        res = []
        tracker = 'n'

        def dfs(i, combo, check):
            if i == (2*n)-1:
                if len(check) == 0:
                    res.append(combo.copy())
                return
            
            combo.append('(')
            check.append('(')
            dfs(i+1, combo, check)
            combo.pop()
            check.pop()
            combo.append(')')
            if len(check) > 0 and check[-1] == '(':
                check.pop()
                tracker = 'y'
            else:
                check.append(')')
                tracker = 'n'
            dfs(i+1, combo, check)
            combo.pop()
            if tracker == 'y':
                check.append('(')
            if tracker == 'n':
                check.pop()


        check = dfs(0, ['('], ['('])
        result = ["".join(inner_list) for inner_list in res]
        return result
            