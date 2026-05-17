class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        for i in nums:
            if seen[i] > 0:
                return i
            else:
                seen[i] += 1
