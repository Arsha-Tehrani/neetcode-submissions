class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] represents the length of the LIS starting at index i.
        # Every element is an increasing subsequence of at least length 1.
        dp = [1] * len(nums)

        # Iterate backwards starting from the end of the array
        for i in range(len(nums) - 1, -1, -1):
            # Look at every element that comes AFTER the current element i
            for j in range(i + 1, len(nums)):
                # If the later element is strictly greater, it can be appended to our sequence
                if nums[j] > nums[i]:
                    # Update dp[i] to be the max of its current value, 
                    # or 1 + the LIS starting at j
                    dp[i] = max(dp[i], 1 + dp[j])

        # The longest sequence could start anywhere, so return the max value in the dp array
        return max(dp)