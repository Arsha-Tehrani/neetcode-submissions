class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            if m > 0 and nums[m] < nums[m-1]:
                return nums[m]
            if nums[0] <= nums[m]:
                l = m+1
            else:
                r = m-1

        return nums[0]

            
