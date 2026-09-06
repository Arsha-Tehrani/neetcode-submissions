class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefix = {0:1}

        for num in nums:
            curSum += num
            dif = (k - curSum) * -1

            res += prefix.get(dif, 0)
            prefix[curSum] = 1 + prefix.get(curSum ,0)

        return res
