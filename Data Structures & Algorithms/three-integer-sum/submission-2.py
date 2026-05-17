class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = len(nums) - 1
        res = []


        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                summ = nums[i] + nums[j]
                dif = 0-summ
                if dif in nums and nums.index(dif) != i and nums.index(dif) != j:
                    temp = [nums[i], nums[j], dif]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)


        return res
