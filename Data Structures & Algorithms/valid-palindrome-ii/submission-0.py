class Solution:
    def validPalindrome(self, s: str) -> bool:
        tol = 0
        l = 0
        r = len(s) - 1

        def move(left, right):
            nonlocal tol
            while left < right:
                if s[right] == s[left]:
                    right -= 1
                    left += 1
                
                elif tol < 1:
                    tol += 1
                    return move(left+1, right) or move(left, right-1)
                
                else:
                    return False
            
            return True

        return move(l, r)