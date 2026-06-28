class Solution:
    def rob(self, nums: List[int]) -> int:
        #I can start at 0 or 1
        #I can make jumps of 2 or 3
        if len(nums) == 1:
            return nums[0]

        for i in range(3, len(nums)+1):
            if -i+3 < 0:
                nums[-i] += max(nums[-i+2], nums[-i+3])
            else:
                nums[-i] += nums[-i+2]

        return max(nums[0], nums[1])