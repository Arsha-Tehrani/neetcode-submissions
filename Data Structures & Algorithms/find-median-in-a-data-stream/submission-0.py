class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n% 2 != 0:
            return self.nums[n//2]
        else:
            x = self.nums[n//2]
            y = self.nums[n//2 - 1]

            return (x+y)/2
        
        