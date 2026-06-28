class Solution:
    def rob(self, nums: List[int]) -> int:
        # Global edge case: If there's only one house, you have to rob it.
        if len(nums) == 1:
            return nums[0]

        # Run the helper on two slices and return the max:
        # 1. nums[:-1] -> Excludes the last house
        # 2. nums[1:]  -> Excludes the first house
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums: List[int]) -> int:
        # Local edge cases for the slices
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Your exact original logic
        for i in range(3, len(nums)+1):
            if -i+3 < 0:
                nums[-i] += max(nums[-i+2], nums[-i+3])
            else:
                nums[-i] += nums[-i+2]

        return max(nums[0], nums[1])