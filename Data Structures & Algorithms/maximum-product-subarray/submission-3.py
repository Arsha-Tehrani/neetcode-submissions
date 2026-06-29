class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #create an array to store results
        #Iterate through. When you hit Negative, branch off. When another negative is hit. collapse them together
        #If hit 0 before the split. just add the result to array and keep goin.
        #If hit 0 after the split then max of split is added. split is ended. and the pre-split max is added.
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp, curMin*n, n)

            res = max(res, curMax)

        return res