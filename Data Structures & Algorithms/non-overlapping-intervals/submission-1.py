class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        fin = 0
        res.append(intervals[0])
        print(intervals)

        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = res[-1]

            if cur[0] < prev[1]:
                prev = res.pop()
                if (prev[1]) > cur[1]:
                    res.append(cur)
                else:
                    res.append(prev)

                fin += 1

            else:
                res.append(cur)

        return fin