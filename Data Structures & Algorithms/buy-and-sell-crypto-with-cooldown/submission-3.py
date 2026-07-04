class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        hold = -float('inf')
        sold = 0
        rest = 0
        
        for price in prices:
            prev_sold = sold
            # If we sell today, we add today's price to whatever we had when we bought
            sold = hold + price
            # We either keep holding what we had, or we buy today (spending 'price' from our rest state)
            hold = max(hold, rest - price)
            # We either keep resting, or we transition into rest because we sold yesterday
            rest = max(rest, prev_sold)
            
        return max(sold, rest)