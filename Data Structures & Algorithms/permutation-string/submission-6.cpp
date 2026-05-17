class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> freq_set;
        unordered_map<char, int> freq_test;

        int left = 0;
        for(char x : s1)
        {
            freq_set[x]++;
        }

        for(int i = 0; i < s2.size(); i++)
        {
            freq_test[s2[i]]++;
            while (freq_test[s2[i]] > freq_set[s2[i]])
            {
                freq_test[s2[left]]--;
                left++;
            }

            if (freq_test == freq_set)
            {
                return true;
            }
        }

        return false;
    }
};
