class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        i = 0
        j = 1

        while i < j and j != n:
            cur = prices[j] - prices[i]
            res = max(cur, res)
            
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                j += 1
                
        return res