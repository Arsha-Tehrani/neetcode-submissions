from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count = Counter(t)
        required = len(count) # Track unique characters needed, not total length
        
        window_counts = defaultdict(int)
        formed = 0 # How many unique characters have met their required frequency
        
        l = 0
        res = float("inf"), 0, 0 # length, left, right
        
        # r is the right pointer
        for r in range(len(s)):
            char = s[r]
            window_counts[char] += 1
            
            # If the frequency of the current character matches what we need
            if char in count and window_counts[char] == count[char]:
                formed += 1
            
            # Phase 2: Shrink the window until it is no longer valid
            while l <= r and formed == required:
                char_left = s[l]
                
                # Update our minimum result
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)
                
                # Remove the left character from our window
                window_counts[char_left] -= 1
                if char_left in count and window_counts[char_left] < count[char_left]:
                    formed -= 1 # The window is no longer valid, we need to expand again
                
                l += 1 # Shrink the window
                
        return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]