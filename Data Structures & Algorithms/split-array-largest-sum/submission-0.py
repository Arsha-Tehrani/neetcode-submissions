class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def valid(limit):
            temp_k = 1
            cur = 0
            i = 0
            while i < len(nums):
                if cur + nums[i] <= limit:
                    cur += nums[i]
                    i += 1
                else:
                    cur = 0
                    temp_k += 1
            
            return temp_k <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            m = (left + right) // 2
            if valid(m):
                right = m
            else:
                left = m + 1

        return left