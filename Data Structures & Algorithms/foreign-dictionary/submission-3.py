class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for word in words for c in word}
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            small = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:small] == w2[:small]:
                return ""

            for j in range(small):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} #False = Completed, True = Visiting
        print(adj)

        res = []

        def dfs(node):
            if node in visit:
                return visit[node]
            
            visit[node] = True

            for nei in adj[node]:
                if dfs(nei):
                    return True

            res.append(node)
            visit[node] = False
            return False

        for key in adj.keys():
            if dfs(key):
                return ""
        
        return str.join("", res[::-1])
                



