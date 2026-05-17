class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> relate;
        relate[']'] = '[';
        relate[')'] = '(';
        relate['}'] = '{';

        vector<char> open_que;
        for (char i : s)
        {
            if (i == '(' or i == '[' or i == '{')
            {
                open_que.push_back(i);
            }
            else if (i == ')' or i == '}' or i == ']')
            {
                if (open_que.size() == 0)
                {
                    return false;
                }
                else if (open_que.back() != relate[i])
                {
                    return false;
                }
                else
                {
                    open_que.pop_back();
                }
            }
        }

        if (open_que.size() == 0)
        {
            return true;
        }

        else
        {
            return false;
        }
    }
};
