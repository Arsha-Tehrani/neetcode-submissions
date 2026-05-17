class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            base = 0
            h = heights[i]
            for l in range(i, -1, -1):
                if heights[l] < h:
                    break
                else:
                    base += 1
            #print(base)
            for r in range(i+1, len(heights)):
                if heights[r] < h:
                    break
                else:
                    base += 1
            #print(base)

            area = base * h
            res = max(res, area)

        return res