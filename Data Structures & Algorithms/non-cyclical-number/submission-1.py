class Solution:
    def isHappy(self, n: int) -> bool:
        db = set()
        while 0 < 1:
            num = str(n)
            res = 0
            for i in num:
                res += int(i) ** 2

            if res in db:
                return False

            if res == 1:
                return True

            db.add(res)
            n = res