//
// ********
// ***  ***
// **      **
// *         *
// *        *
// **     **
// ***  ***
// ********
#include <iostream>
using namespace std;
int main()
{
  int n;
  cout << "Enter the number n" << endl;
  cin >> n;
  for (int i = n; i >= 1; i--)
  {
    for (int j = 1; j <= n; j++)
    {
      if (i >= j)
        cout << "*";
    }
    for (int k = 1; k <= n - i; k++)
      cout << "  ";
    for (int l = i; l >= 1; l--)
    {
      cout << "*";
    }
    cout << endl;
  }

  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= i; j++)
    {
      cout << "*";
    }
    for (int k = i; k <= n - 1; k++)
    {

      cout << "  ";
    }
    for (int l = i; l >= 1; l--)
    {
      cout << "*";
    }
    cout << endl;
  }
}