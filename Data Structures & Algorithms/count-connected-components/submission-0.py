class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        tot = 0

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            
            for x in adj[node]:
                dfs(x)

        for i in range(n):
            if i not in visited:
                dfs(i)
                tot += 1

        return tot