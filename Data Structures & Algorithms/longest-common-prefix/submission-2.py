class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = strs[0]

        for i in range(1, len(strs)):
            trig = False
            if len(strs[i]) == 0: return ""

            for j in range(len(min(cur, strs[i]))):
                if cur[j] != strs[i][j]:
                    trig = True
                    cur = cur[:j]
                    break
            
            if not trig:
                cur = min(cur, strs[i])
                
        return cur