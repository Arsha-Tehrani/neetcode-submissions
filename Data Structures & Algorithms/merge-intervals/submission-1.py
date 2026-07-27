class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = res[-1]
            if cur[0] <= prev[1]:
                prev = res.pop()
                new = [min(cur[0], prev[0]), max(cur[1], prev[1])]
                res.append(new)

            else:
                res.append(cur)

        return res