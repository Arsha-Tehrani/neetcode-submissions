class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        req = defaultdict(set)
        for i in prerequisites:
            req[i[0]].add(i[1])

        built = set()
        fin = defaultdict(set)
        def builder(course):
            nonlocal fin
            nonlocal built

            if course in built:
                return fin[course]
            if course in req:
                for sub in req[course]:
                    fin[course].add(sub)
                    fin[course].update(builder(sub))
                built.add(course)
                return fin[course]
            
            elif course not in req:
                return [course]

        for i in req:
            builder(i)

        res = []
        for i in queries:
            if i[1] in fin[i[0]]:
                res.append(True)
            else:
                res.append(False)

        return res
        