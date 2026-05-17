"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        if not cur:
            return None
        first = Node(x = head.val)
        res = first
        created = defaultdict(int)
        created[cur] = first
        while cur:
            if cur.next and created[cur.next] == 0:
                first.next = Node(cur.next.val)
                created[cur.next]  = first.next
            elif cur.next and created[cur.next] != 0:
                first.next = created[cur.next]
            else:
                first.next = None
            if cur.random and created[cur.random] == 0:
                first.random = Node(cur.random.val)
                created[cur.random] = first.random
            elif cur.random and created[cur.random] != 0:
                first.random = created[cur.random]
            else:
                first.random = None
            
            first = first.next
            cur = cur.next

        return res