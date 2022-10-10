#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void rotate(vector<vector<int>> &matrix)
{
    int n = matrix.size();
    // transpose
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            swap(matrix[i][j], matrix[j][i]);
        }
    }

    // reverse the rows
    for (int i = 0; i < n; i++)
    {
        reverse(matrix[i].begin(), matrix[i].end());
    }
}

void print_matrix(vector<vector<int>> matrix)
{
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size(); j++)
        {
            cout << matrix[i][j] << "   ";
        }
        cout << endl;
    }
}

int main()
{
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}};
    cout << "initial matrix" << endl;
    print_matrix(matrix);
    rotate(matrix);
    cout << "rotated matrix" << endl;
    print_matrix(matrix);
}
