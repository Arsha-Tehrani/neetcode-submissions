class Solution:
    def isHappy(self, n: int) -> bool:
        db = set()
        def help(n):
            res = 0
            while n > 0:
                cur = n % 10
                res += cur * cur
                n = n // 10
            return res
        
        while n != 1:
            res = help(n)

            if res in db:
                return False
            
            db.add(res)
            n = res
        return True