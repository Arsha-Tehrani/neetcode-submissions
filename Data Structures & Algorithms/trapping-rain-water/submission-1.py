class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = height[0]
        r_max = height[n-1]
        l = 0
        r = n-1
        res = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                if min(l_max, r_max) - height[l] > 0:
                    res += min(l_max, r_max) - height[l]
                l_max = max(l_max, height[l])

            else:
                r -= 1
                if min(l_max, r_max) - height[r] > 0:
                    res += min(l_max, r_max) - height[r]
                r_max = max(r_max, height[r])

        return res

            

        