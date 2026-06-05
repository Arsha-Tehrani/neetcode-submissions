from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)

        # 2. Use your exact sets
        done = set()
        taking = set()

        def dfs(course):
            # If we've already cleared this course, it's safe
            if course in done:
                return True
            # If we hit a course we are currently taking, we found a cycle!
            if course in taking:
                return False

            # Mark course as currently being explored
            taking.add(course)
            
            # Check all prerequisites
            for req in adj[course]:
                if not dfs(req):
                    return False # EARLY EXIT: Stop looping instantly if a cycle is found

            # We finished all prerequisites. Clean up and mark as done.
            taking.remove(course)
            done.add(course)
            return True

        # 3. Check every course (handles disconnected graphs)
        for i in range(numCourses):
            if not dfs(i):
                return False # If any course fails, we can't finish

        return True