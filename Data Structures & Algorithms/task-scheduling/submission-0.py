class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        time = 0
        line = deque()

        while heap or line:
            time += 1

            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    line.append((time + n, cnt))

            if line and line[0][0] == time:
                heapq.heappush(heap, line.popleft()[1])

        return time
                
                
