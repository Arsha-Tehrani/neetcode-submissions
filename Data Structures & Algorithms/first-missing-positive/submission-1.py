class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        for i in range(len(nums)):
            if nums[i] <= 0 or (i > 0 and nums[i-1] == nums[i]):
                continue
            
            if nums[i] != count:
                return count
            
            count += 1

        return count