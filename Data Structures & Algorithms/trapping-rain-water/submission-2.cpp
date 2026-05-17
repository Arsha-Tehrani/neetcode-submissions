class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int l = 0;
        int r = n-1;
        int r_max = height[r];
        int l_max = height[l];
        int res = 0;

        while (l < r)
        {
            if (height[l] < height[r])
            {
                l++;
                if (min(l_max, r_max) - height[l] > 0)
                {
                    res += min(l_max, r_max) - height[l];
                }

                l_max = max(l_max, height[l]);
            }

            else
            {
                r--;
                if (min(l_max, r_max) - height[r] > 0)
                {
                    res += min(l_max, r_max) - height[r];
                }

                r_max = max(r_max, height[r]);
            }
        }

        return res;
    }
};
