class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []

        def dive(position, total):

            if total == target:
                res.append(list(temp))
                return 

            elif total > target or position >= len(nums):
                return 

            temp.append(nums[position])
            dive(position, total + nums[position])
            temp.pop()
            dive(position + 1, total)

        dive(0, 0)
        return res




