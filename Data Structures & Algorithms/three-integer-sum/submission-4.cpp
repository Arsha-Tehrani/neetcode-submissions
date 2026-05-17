class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int r, l, sum;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++)
        {
            if (i > 0 and nums[i] == nums[i-1])
            {
                continue;
            }

            l = i+1;
            r = nums.size()-1;

            while (l < r)
            {
                sum = nums[i] + nums[l] + nums[r];
                if (sum > 0)
                {
                    r--;
                }
                else if (sum < 0)
                {
                    l++;
                }
                else
                {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    while (l < r and nums[l] == nums[l-1])
                    {
                        l++;
                    }
                }
            }
        }

        return res;
    }
};
