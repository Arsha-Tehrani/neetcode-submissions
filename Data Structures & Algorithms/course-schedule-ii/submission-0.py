class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for i in prerequisites:
            adj[i[0]].add(i[1])

        print(adj)
        done = set()
        taking = set()
        starting = []

        def dfs(course):
            if course in taking:
                taking.add(-1)
                return False
            if course in done:
                return True

            taking.add(course)

            for req in adj[course]:
                dfs(req)

            done.add(course)
            taking.remove(course)
            starting.append(course)

        

        for course in range(numCourses):
            dfs(course)

        if -1 in taking:
            return []

        return starting