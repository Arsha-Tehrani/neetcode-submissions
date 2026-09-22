import heapq

class FreqStack:
    def __init__(self):
        self.heap = []
        self.count = {}
        # This replaces your self.stack array. It tracks the exact order elements arrive.
        self.push_index = 0 

    def push(self, val: int) -> None:
        # Increment frequency
        self.count[val] = self.count.get(val, 0) + 1
        
        # Increment our push index for recency
        self.push_index += 1
        
        # Push to max-heap: 
        # 1. -count (highest frequency first)
        # 2. -push_index (most recently pushed first, acting as our tie-breaker)
        # 3. val (the actual value to return)
        heapq.heappush(self.heap, (-self.count[val], -self.push_index, val))

    def pop(self) -> int:
        # The heap automatically surfaces the most frequent, most recent item
        freq, push_idx, val = heapq.heappop(self.heap)
        
        # Decrement the actual frequency count!
        self.count[val] -= 1
        
        return val