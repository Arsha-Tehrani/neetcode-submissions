class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i in prerequisites:
            adj[i[0]].append(i[1])

        print(adj)
        done = set()
        taking = set()
        for i in range(numCourses):
            if i not in adj:
                done.add(i)

        print(done)
        def dfs(course):
            fin = True
            if course in done:
                return True
            if course in taking:
                done.add(-1)
                return False

            taking.add(course)
            
            for req in adj[course]:
                if not dfs(req):
                    fin = False

            if fin:
                taking.remove(course)
                done.add(course)
                return True

        for course in adj:
            if len(done) != numCourses:
                dfs(course)

        if -1 in done:
            return False
        if len(done) == numCourses:
            return True
