class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp = [-s for s in stones]
        heapq.heapify(temp)

        while len(temp) > 1:    
            y = (-1)*heapq.heappop(temp)
            x = (-1)*heapq.heappop(temp)

            if x < y:
                new = -(y-x)
                heapq.heappush(temp, new)

        if len(temp) == 1:
            return (-1)*heapq.heappop(temp)
        return 0