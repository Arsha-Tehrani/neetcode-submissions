class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        res = []
        for i in range(len(edges)+1):
            parents[i] = i

        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return x

        def union(x, y):
            parents[find(x)] = find(y)

        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                res.append(edge)

            union(edge[0], edge[1])
        
        return res[-1]