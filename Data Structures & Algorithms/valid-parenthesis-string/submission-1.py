class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for i in s:
            if i == "(":
                high += 1
                low += 1

            elif i == ")":
                high -= 1
                low -= 1

            else:
                high += 1
                low -= 1

            if high < 0:
                return False

            if low < 0:
                low = 0

        return low == 0