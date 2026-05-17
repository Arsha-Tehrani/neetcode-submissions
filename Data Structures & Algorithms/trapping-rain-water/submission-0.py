class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n):
            r_max = 0
            l_max = 0
            for right in range(i):
                cur = height[right]
                r_max = max(r_max, cur)
            
            for left in range(n-i-1):
                cur = height[left+1+i]
                l_max = max(cur, l_max)

            if min(r_max, l_max) - height[i] > 0:
                res += min(r_max, l_max) - height[i]

        return res