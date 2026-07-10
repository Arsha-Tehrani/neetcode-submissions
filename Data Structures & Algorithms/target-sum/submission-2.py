class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        res = 0
        def backtrack(i, total):
            nonlocal res
            if total == target and i == len(nums) - 1:
                res += 1
                return 

            if i < len(nums) - 1:
                backtrack(i+1, total + nums[i+1])
                backtrack(i+1, total - nums[i+1])

        backtrack(0,nums[0])
        backtrack(0,-nums[0])
        return res