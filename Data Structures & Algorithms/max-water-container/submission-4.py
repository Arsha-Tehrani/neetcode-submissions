class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        start = 0
        end = len(heights) - 1
        while end > start:
            cur = min(heights[start], heights[end]) * (end-start)
            res = max(cur, res)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return res