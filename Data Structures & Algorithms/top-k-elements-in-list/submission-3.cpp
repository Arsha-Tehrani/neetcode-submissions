class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int i : nums)
        {
            count[i]++;
        }

        vector<vector<int>> freq(nums.size() + 1);
        for (auto& p : count)
        {
            int key = p.first;
            int value = p.second;
            freq[value].push_back(key);
        }

        vector<int> final;
        for (int n = freq.size()-1; n>=0; n--)
        {
            for (int j : freq[n])
            {
                final.push_back(j);
                if (final.size() == k)
                {
                    return final;
                }
            }
        }
    }
};
