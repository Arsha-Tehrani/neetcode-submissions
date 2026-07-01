class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        db = [False] * (len(s))        
        set(wordDict)
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict and j+1 == len(s):
                    db[i] = True
                elif s[i:j+1] in wordDict and db[j+1] == True:
                    db[i] = True
                    break
                elif s[i:j+1] in wordDict:
                    db[i] = False
                    

        return db[0]
