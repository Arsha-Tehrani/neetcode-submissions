class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = int(len(nums) / 2)
        if not nums:
            return -1

        if nums[middle] == target:
            return middle
        if len(nums) <= 1:
            return -1
        elif nums[middle] > target:
            nums = nums[:middle]
            return self.search(nums, target)

        elif nums[middle] < target:
            nums = nums[middle+1:]
            res = self.search(nums, target)
            if res == -1:
                return -1
            else:
                return middle + res + 1
