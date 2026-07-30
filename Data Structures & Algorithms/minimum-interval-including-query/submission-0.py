class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for i in range(len(intervals)):
            left = intervals[i][0]
            right = intervals[i][1]
            intervals[i] = [left, right, right-left+1]

        for i in queries:
            m = float("inf")
            for j in intervals:
                left = j[0]
                right = j[1]
                size = j[2]
                if i >= left and i <= right:
                    m = min(m, size)

            if m == float("inf"):
                m = -1
            
            res.append(m)
        
        return res
