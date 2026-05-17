class Solution {
public:
    bool checkbox(vector<vector<char>>& board, int i, int j) 
        {
            unordered_map<char, int> box;
            for (int r = 0; r < 3; r++) 
            {
                for (int c = 0; c < 3; c++) 
                {
                    char slot = board[r+i][c+j];
                    if (slot != '.')
                    {
                        box[slot]++;
                        if (box[slot] > 1)
                        {
                            return false;
                        }
                    }
                }
            }

            if ((j+3) < 9)
            {
                return checkbox(board, i, j+3);
            }
            if ((i+3) < 9)
            {
                return checkbox(board, i+3, 0);
            }

            return true;

        }


    bool isValidSudoku(vector<vector<char>>& board) {
        //Check Row/Col Repitions
        for (int i = 0; i<9; i++)
        {
            unordered_map<char, int> row;
            unordered_map<char, int> col;

            for (int j = 0; j < 9; j++)
            {
                char slot_row = board[i][j];
                char slot_col = board[j][i];
                if (slot_row != '.')
                {
                    row[slot_row]++;
                    if (row[slot_row] > 1)
                    {
                        return false;
                    }
                }

                if (slot_col != '.')
                {
                    col[slot_col]++;
                    if (col[slot_col] > 1)
                    {
                        return false;
                    }
                }
            }
        }

        //Box Check 
        

        return checkbox(board, 0, 0);
    }
};
