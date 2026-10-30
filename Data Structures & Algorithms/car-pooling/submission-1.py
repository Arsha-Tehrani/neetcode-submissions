class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []

        trips.sort(key= lambda x:x[1])

        for trip in trips:
            if len(heap) == 0:
                if trip[0] > capacity:
                    return False
                
                heapq.heappush(heap, (trip[2], trip[0]))
                capacity -= trip[0]
            
            else:

                while len(heap) > 0 and heap[0][0] <= trip[1]:
                    temp = heapq.heappop(heap)
                    capacity += temp[1]

                if trip[0] > capacity:
                    return False
                
                heapq.heappush(heap, (trip[2], trip[0]))
                capacity -= trip[0]

        return True
