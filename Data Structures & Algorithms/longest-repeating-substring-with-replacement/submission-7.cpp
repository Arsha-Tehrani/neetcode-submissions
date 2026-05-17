#include <algorithm>
class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        int max_freq = 0;
        int n = s.size();
        int res = 0;
        unordered_map<char,int> freq;

        for (int r = 0; r < n ; r++)
        {
            freq[s[r]]++;
            max_freq = max(max_freq, freq[s[r]]);

            while ((r - left + 1)-max_freq > k)
            {
                freq[s[left]]--;
                left++;

            }

            res = max(res, (r-left+1));
        }

        return res;
    }
};
