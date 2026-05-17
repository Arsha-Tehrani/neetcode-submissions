class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (string s : strs)
        {
            string key = s;
            sort(key.begin(), key.end());
            groups[key].push_back(s);
        }

        vector<vector<string>> final;
        for (auto& entry: groups)
        {
            final.push_back(entry.second);
        }

        return final;
    }
};
