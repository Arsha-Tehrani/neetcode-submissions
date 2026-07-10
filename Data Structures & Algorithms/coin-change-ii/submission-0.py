from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Make dp. rows = len(coins) + 1, columns = amount + 1
        dp = [[0] * (amount + 1) for i in range(len(coins) + 1)]

        # Base case: 1 way to make an amount of 0 (use no coins)
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        # Build the DP table bottom-up
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                # If the coin is larger than the current amount, we can't use it
                if j - coins[i] < 0:
                    dp[i][j] = 0
                else:
                    # Number of ways if we DO use the current coin
                    dp[i][j] = dp[i][j - coins[i]]

                # Add the number of ways if we SKIP the current coin
                dp[i][j] += dp[i+1][j]

        # The result is the number of ways to make 'amount' using all coins (starting from index 0)
        return dp[0][amount]