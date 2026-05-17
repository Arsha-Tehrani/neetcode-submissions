class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        i = 0
        res = 0
        
        passed = set()
        passed.add(s[0])

        for j in range(1,len(s)):
            while s[j] in passed:
                passed.remove(s[i])
                i += 1

            passed.add(s[j])
            res = max(res, len(passed))

        return res
