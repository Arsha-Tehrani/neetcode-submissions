class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        res = ""
        while left < len(word1) and right < len(word2):
            res += word1[left]
            res += word2[right]
            left += 1
            right += 1
        
        if left == len(word1):
            res += word2[right:]
        else:
            res += word1[left:]

        return res