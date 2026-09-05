class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = False
        res = 0
        cur = 0
        for i in range(len(prices)):
            if holding == False:
                holding = True
                cur = prices[i]
            
            if holding == True and  i < (len(prices) - 1) and prices[i+1] < prices[i]:
                holding = False
                res += prices[i] - cur
            
        if holding == True:
            res += prices[-1] - cur

        return res
