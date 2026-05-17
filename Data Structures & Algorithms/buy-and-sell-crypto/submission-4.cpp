class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //
        int low = 999;
        int res = 0;

        for (int i = 0; i < prices.size(); i++)
        {
            low = min(low, prices[i]);
            res = max(res, (prices[i] - low));
        }

        return res;
    }
};
