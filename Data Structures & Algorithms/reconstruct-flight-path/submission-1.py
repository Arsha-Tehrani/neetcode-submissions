class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)        
        for i in tickets:
            adj[i[0]].append(i[1])
            
        # FIXED 1: Added sorting to satisfy the lexicographical order rule
        for key in adj:
            adj[key].sort()

        cur = ["JFK"]
        res = []

        def dfs(place):            
            if len(cur) == len(tickets) + 1:
                res.append(cur.copy())
                # FIXED 2: Removed `cur = ["JFK"]`. Backtracking (cur.pop) handles cleanup.
                # FIXED 3: Changed `return` to `return True` so the caller knows to stop.
                return True

            if len(res) == 0:
                for dest in range(len(adj[place])):
                    temp = adj[place][dest]
                    if temp == "skip":
                        continue

                    adj[place][dest] = "skip"
                    cur.append(temp)
                    if dfs(temp):
                        return True
                    adj[place][dest] = temp
                    cur.pop()

                return False

        dfs("JFK")
        # FIXED 4: Returned the actual path array instead of printing a nested list
        return res[0]
