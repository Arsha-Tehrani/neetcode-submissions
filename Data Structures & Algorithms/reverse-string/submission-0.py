class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s) // 2 - 1
        if len(s) % 2 == 0:
            r = len(s) // 2
        else:
            r = len(s)//2 + 1
            
        while r < len(s):
            s[l], s[r] = s[r], s[l]

            r += 1
            l -= 1
