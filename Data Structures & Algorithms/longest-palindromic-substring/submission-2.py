class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return (left+1, right-1)

        val = 0
        word = ""
        
        for i in range(len(s)):
            c1 = expand(i,i)
            w1 = s[c1[0] : c1[1]+1]
            c2 = expand(i,i+1)
            w2 = s[c2[0] : c2[1]+1]
            len1 = len(w1) #Check for odds
            len2 = len(w2) #check for evens 

            if len1 > len2:
                big = len1
                temp = w1
            else:
                big = len2
                temp = w2

            if big > val:
                val = big
                word = temp

        return word