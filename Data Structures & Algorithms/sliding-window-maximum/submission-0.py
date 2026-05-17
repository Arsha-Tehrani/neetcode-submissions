class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for l in range(len(nums)-k+1):
            r = l + k
            cur = float('-inf')

            for i in range(l, r):
                if nums[i] > cur:
                    cur = nums[i]

            res.append(cur)

        return res