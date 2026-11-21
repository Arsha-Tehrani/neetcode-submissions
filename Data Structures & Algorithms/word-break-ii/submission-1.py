class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        results = []
        temp = []
        def back(start_i):
            nonlocal temp
            nonlocal results
            if start_i == len(s):
                results.append(temp.copy())

            cur = ""
            for ind in range(start_i, len(s)):
                cur += s[ind]
                if cur in wordSet:
                    temp.append(cur)
                    back(ind+1)
                    temp.pop()

        back(0)
        #print(results)
        res = []
        for sentance in results:
            cur = " ".join(sentance)
            res.append(cur)

        return res