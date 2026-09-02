class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
                
            temp = target - nums[i]
            if temp in dic and dic[temp] != i:
                if i < dic[temp]: return [i, dic[temp]]

                return [dic[temp], i]

        return None
