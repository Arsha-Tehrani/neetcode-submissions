class Solution {
public:
    int jump(vector<int>& nums) {
        int res = 0;
        int q = nums.size();
        int r = 0; 
        int l = 0;
        int furthest;

        while(r < q-1)
        {
            furthest = 0;
            for(int i = l; i < r+1; i++)
            {
                furthest = max(furthest, i + nums[i]);
            }
            l = r+1;
            r = furthest;
            res++;
        }

        return res;
    }
};
