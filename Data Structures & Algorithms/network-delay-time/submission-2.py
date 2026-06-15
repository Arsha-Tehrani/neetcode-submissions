class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        #make an adjacency list
        adj = defaultdict(list)
        for path in times:
            adj[path[0]].append((path[2], path[1]))

        visited = set()
        order = [(0, k)]
        heapq.heapify(order)
        res = 0

        while order:
            top = heapq.heappop(order)
            if top[1] in visited:
                continue
            visited.add(top[1])
            res = top[0]
            for x in adj[top[1]]:
                heapq.heappush(order, (x[0] + res, x[1]))

        if len(visited) == n:
            return res
        return -1