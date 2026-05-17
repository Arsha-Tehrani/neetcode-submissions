class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        r = 0
        res = 0
        max_freq = 0

        for i in range(len(s)):
            freq[s[i]] += 1
            max_freq = max(max_freq, freq[s[i]])
            
            while (i - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, i-l+1)

        return res