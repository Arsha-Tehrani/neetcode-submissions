class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for edge in flights:
            adj[edge[0]].append((edge[1], edge[2])) #First node then cost

        res = float("inf")
        done = False

        stack = [] #entries are tuples. 1st - Trail cost. 2nd - Apirport. 3rd - stops
        heapq.heapify(stack)

        for i in adj[src]:
            tup = (i[1], i[0], 0)
            heapq.heappush(stack, tup)

        while stack:
            cur = heapq.heappop(stack)
            if cur[2] > k:
                continue
            if cur[1] == dst:
                return cur[0]

            for nei in adj[cur[1]]:
                heapq.heappush(stack, (cur[0]+nei[1], nei[0], cur[2]+1))

        return -1