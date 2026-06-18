class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        
        # 1. Use simple arrays for Union-Find instead of dicts with tuples
        parents = list(range(n))
        rank = [1] * n # Optional but good practice: union by rank

        def find(i):
            if parents[i] == i:
                return i
            # Path compression: update the parent to the root
            parents[i] = find(parents[i]) 
            return parents[i]

        def union(i, j):
            p1 = find(i)
            p2 = find(j)

            if p1 == p2:
                return False
                
            # Union by rank keeps the tree shallow
            if rank[p1] > rank[p2]:
                parents[p2] = p1
            elif rank[p1] < rank[p2]:
                parents[p1] = p2
            else:
                parents[p2] = p1
                rank[p1] += 1
            return True

        # 2. Prevent duplicates by only checking j > i
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        # Sorting a list is generally faster than N^2 heappushes in Python
        edges.sort()

        res = 0
        edges_used = 0
        
        for dist, i, j in edges:
            if union(i, j):
                res += dist
                edges_used += 1
                
                # 3. Early termination: we only need N - 1 edges to connect N points
                if edges_used == n - 1:
                    break
                    
        return res