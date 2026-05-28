"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        store = {}

        def clone(node):
            if node in store:
                return store[node]

            copy = Node(node.val)
            store[node] = copy
            for n in node.neighbors:
                temp = clone(n)
                copy.neighbors.append(temp)

            return copy
        
        if node:
            return clone(node)
        else:
            return None