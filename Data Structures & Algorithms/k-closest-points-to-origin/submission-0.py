class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            dist = (points[i][0]**2 + points[i][1]**2)**(1/2)
            points[i] = [dist, points[i][0], points[i][1]]

        heapq.heapify(points)
        res = []
        for i in range(k):
            cur = heapq.heappop(points)
            res.append(cur[1:])


        return res