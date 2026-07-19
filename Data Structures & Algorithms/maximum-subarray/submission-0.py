class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = {}
        cache[len(nums)-1] = nums[-1]
        res = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            cache[i] = max(nums[i], nums[i] + cache[i+1])
            res = max(res, cache[i])

        return res