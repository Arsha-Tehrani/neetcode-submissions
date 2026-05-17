import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # Max-Heap (stores negative numbers)
        self.right = []  # Min-Heap (stores positive numbers)

    def addNum(self, num: int) -> None:
        # 1. Routing: If left is empty OR num belongs in the lower half
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        # 2. Rebalancing: Ensure Left is exactly equal to, or 1 larger than, Right
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
            
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
        
    def findMedian(self) -> float:
        total_len = len(self.left) + len(self.right)
        
        if total_len % 2 == 0:
            middle = self.right[0] + (self.left[0] * -1)
            return middle / 2.0
        else:
            return float(self.left[0] * -1)