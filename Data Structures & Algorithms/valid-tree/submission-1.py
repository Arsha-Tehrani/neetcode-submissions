class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(set)
        pee = set()

        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])

        print(adj)

        def dfs(node, origin):
            if (origin, node) in pee:
                return
            if node in visited or -1 in visited:
                visited.add(-1)
                return

            pee.add((node, origin))

            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor, node)

        print(visited)
        visited.add(0)
        for x in adj[0]:
            dfs(x, 0)
        
        if -1 in visited:
            return False

        if len(visited) == n:
            return True
        
        return False