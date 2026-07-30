class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)
        for i in range(len(intervals)):
            left = intervals[i][0]
            right = intervals[i][1]
            intervals[i] = [left, right, right-left+1]

        for i in range(len(queries)):
            queries[i] = [queries[i], i]

        intervals.sort()
        queries.sort()

        for i in queries:
            ind = i[1]
            val = i[0]
            m = float("inf")
            for j in intervals:
                left = j[0]
                right = j[1]
                size = j[2]
                if left > val:
                    break
                if val >= left and val <= right:
                    m = min(m, size)

            if m == float("inf"):
                m = -1
            
            res[ind] = m
        
        return res
