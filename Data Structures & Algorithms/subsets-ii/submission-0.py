class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, remain):
            if len(remain) == 0:
                res.append(cur.copy())
            
            if i >= len(remain):
                return

            else:
                #use this num
                cur.append(remain[i])
                temp = remain.pop(i)
                dfs(i, cur, remain)
                cur.pop()
                remain.insert(i, temp)
                # skip this and all like it
                while i+1 < len(remain) and remain[i] == remain[i+1]:
                    i += 1
                dfs(0, cur, remain[i+1:])

        dfs(0, [], nums)
        return res