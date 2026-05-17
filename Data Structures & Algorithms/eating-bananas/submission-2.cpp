class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int upper = 0;
        for(int i : piles)
        {
            upper = max(upper,i);
        }

        int r = upper;
        int l = 1;
        int m;
        int time_taken = 0;
        int res;

        while(l <= r)
        {
            m = l + (r-l)/2;
            time_taken = 0;

            for(int i : piles)
            {
                time_taken += (i + m - 1) / m;
            }

            if (time_taken > h)
            {
                l = m+1;
            }
            else
            {
                res = m;
                r = m-1;
            }
        }

        return res;
    }
};
