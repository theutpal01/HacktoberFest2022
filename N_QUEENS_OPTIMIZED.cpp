#include <iostream>
#include <vector>

using namespace std;
class Solution
{
public:
    void process(int col, vector<string> &board, vector<vector<string>> &result, vector<int> &left, vector<int> &diag1, vector<int> &diag2, int size)
    {
        if (col == size)
        {
            result.push_back(board);
            return;
        }
        for (int row = 0; row < size; row++)
        {
            if (left[row] == 0 && diag2[row + col] == 0 && diag1[size - 1 + col - row] == 0)
            {
                board[row][col] = 'Q';
                left[row] = 1;
                diag1[size - 1 + col - row] = 1;
                diag2[row + col] = 1;

                process(col + 1, board, result, left, diag1, diag2, size); // recurse

                board[row][col] = '.';
                left[row] = 0;
                diag1[size - 1 + col - row] = 0;
                diag2[row + col] = 0;
            }
            // else : ignore
        }
        return;
    }

public:
    vector<vector<string>> NQueens(int n)
    {
        vector<vector<string>> result;
        vector<string> vec(n); // board
        string s(n, '.');
        for (int i = 0; i < n; i++)
        {
            vec[i] = s;
        }
        vector<int> left(n, 0), diag1(2 * n - 1, 0), diag2(2 * n - 1, 0);
        process(0, vec, result, left, diag1, diag2, n);
        return result;
    }
};

void printBoard(vector<vector<string>> vec)
{
    for (int i = 0; i < vec.size(); i++)
    {
        cout << "Quuen Positioning/Setup - " << i + 1 << '\n';
        for (int j = 0; j < vec[0].size(); j++)
        {
            cout << vec[i][j] << '\n';
        }
        cout << endl;
    }
    return;
}

int main()
{
    Solution ref;
    int len;
    cin >> len;
    vector<vector<string>> result = ref.NQueens(len);
    printBoard(result);
    return 0;
}