class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        k = 0

        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
                k += 1
            
            if nums[start] != val:
                start += 1

        res = len(nums) - k
        nums = nums[:k]
        
        return res