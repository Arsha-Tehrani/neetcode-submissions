class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m



        pivot = l
        l = 0
        r = len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (r+l)//2
            if nums[m] == target:
                return m
            
            if target > nums[m]:
                l = m+1
            else:
                r = m-1

        return -1