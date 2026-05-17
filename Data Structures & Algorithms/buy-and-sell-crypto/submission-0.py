class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            cur = max(prices[i+1:]) - prices[i]
            res = max(res, cur)

        return res