class Solution:
    def canJump(self, nums: List[int]) -> bool:
        db = [0] * len(nums)
        db[len(nums)-1] = 1

        for i in range(len(nums)-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i+j >= len(nums):
                    break
                
                if db[i+j] == 1:
                    db[i] = 1
                    break

        return db[0] == 1 or False



