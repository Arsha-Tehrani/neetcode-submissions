class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Remove all negative numbers
        i = 0
        method1 = True
        while i < len(nums):
            if nums[i] > len(nums) or nums[i] <= 0:
                i += 1
                continue
            
            ind = nums[i] - 1
            if nums[i] != nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
            
            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        return len(nums) + 1