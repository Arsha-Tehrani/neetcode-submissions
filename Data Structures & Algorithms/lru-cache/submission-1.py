class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lhs, self.rhs = Node(0,0), Node(0,0)
        self.lhs.nxt, self.rhs.prev = self.rhs, self.lhs

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev_last = self.rhs.prev
        self.rhs.prev = node
        prev_last.nxt = node
        node.prev = prev_last
        node.nxt = self.rhs

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            least_node = self.lhs.nxt
            self.remove(least_node)
            del self.cache[least_node.key]


