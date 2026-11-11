class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        def fil(start):
            nonlocal temp
            if len(temp) == k:
                res.append(temp.copy())
                return
            for i in range(start, n+1):
                temp.append(i)
                fil(i + 1)
                temp.pop()

        fil(1)
        return res