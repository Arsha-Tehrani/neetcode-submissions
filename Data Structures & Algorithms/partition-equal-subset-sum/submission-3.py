class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        overall = sum(nums)
        target = overall / 2
        if target != int(target):
            return False

        def dfs(targ, ind):
            if targ == 0:
                return True

            if targ < 0 or ind == len(nums):
                return False

            return dfs(targ - nums[ind], ind + 1) or dfs(targ, ind + 1)


        return dfs(target, 0)