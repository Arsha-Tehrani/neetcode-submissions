class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set(nums)
        return len(nums) != len(check)