class Solution:
    def jump(self, nums: List[int]) -> int:
        
        nums[len(nums)-1] = 0

        for i in range(len(nums)-2, -1, -1):
            #print(nums)
            j = nums[i]
            if i+j >= len(nums)-1:
                nums[i] = 1
            elif j == 0:
                nums[i] = float("inf")
            else:
                nums[i] = min(nums[i+1:i+j+1]) + 1

        #print(nums)
        return nums[0]