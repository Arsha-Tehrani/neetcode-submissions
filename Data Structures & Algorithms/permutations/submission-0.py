class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        res = []

        def dfs(cur, remain):
            if len(remain) == 0:
                res.append(cur.copy())

            for i in range(len(remain)):
                cur.append(remain[i])
                temp = remain.pop(i)
                dfs(cur, remain)
                remain.insert(i, temp)
                cur.pop()

        dfs([], nums)
        
        return res