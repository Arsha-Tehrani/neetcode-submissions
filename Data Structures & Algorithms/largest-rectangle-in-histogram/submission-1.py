class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # pair(index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, (height * (i - index)))
                start = index
            stack.append([start, h])

        for i in stack:
            area = i[1] * (len(heights) - i[0])
            res = max(res, area)

        return res

            