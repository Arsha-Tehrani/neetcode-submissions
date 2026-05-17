class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = list(s)

        i = 0
        res = 0
        
        passed = set()
        passed.add(l[0])

        for j in range(1,len(l)):
            while l[j] in passed:
                passed.remove(l[i])
                i += 1

            passed.add(l[j])
            res = max(res, len(passed))

        return res
