class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l = 0
        r = len(nums)-1
        while l <= r:
            middle = l + int((r-l)/2)
            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle

        return -1
