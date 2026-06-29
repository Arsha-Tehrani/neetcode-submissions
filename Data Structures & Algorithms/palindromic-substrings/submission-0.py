class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        def expand(left, right):
            num = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                num += 1
                left -= 1
                right += 1

            return num

        res = 0
        for i in range(len(s)):
            res += expand(i, i)
            
            res += expand(i, i+1)

        return res