class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = list(s)

        i = 0
        j = 1
        res = 0
        cur = 1
        passed = set()
        passed.add(l[0])

        while i < j and j < len(s):
            if l[j] not in passed:
                cur += 1
                passed.add(l[j])
                j += 1
                

            else:
                i += 1
                j = i+1
                passed. clear()
                passed.add(l[i])
                res = max(res, cur)
                cur = 1

        return max(res, cur)