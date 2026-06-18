class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dest in sorted(tickets, reverse = True):
            adj[src].append(dest)

        res = []

        def dfs(place):
            while adj[place]:
                nxt = adj[place].pop()
                dfs(nxt)

            res.append(place)

        dfs("JFK")
        return res[::-1]
                