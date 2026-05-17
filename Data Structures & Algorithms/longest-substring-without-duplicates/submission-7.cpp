class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char>  passed;

        if (s.size() == 0)
        {
            return 0;
        }
        if (s.size() == 1)
        {
            return 1;
        }

        int i = 0;
        int res = 0;
        passed.insert(s[0]);

        for (int j = 1; j < s.size(); j++)
        {
            while (passed.count(s[j]))
            {
                passed.erase(s[i]);
                i++;
            }

            passed.insert(s[j]);

            res = max(static_cast<int>(passed.size()), res);
        }

        return res;
    }
};
