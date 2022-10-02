// hollow diamond pattern using c++
// creator - namratabose32

//n=5
//     *
//    * *
//   *   *
//  *     *
// *       *
//  *     *
//   *   *
//    * *
//     *


#include <iostream>
using namespace std;

int main() {
  int number, i, j, k=0;
  cin>> number;
  // upper half of diamond
  for (i = 1; i <= number; i++)
  {
    for (j = 1; j <= number-i; j++)
    {
      cout << " " ;
    }
    while (k != (2*i-1))
    {
      if (k == 0 || k == 2*i-2)
      cout << "*" ;
      else 
      cout << " " ;
      k++;
    }
    k = 0;
    cout << endl;
  }
  // lower half of diamond
    number--;
    for (i = number; i >= 1; i--)
    {
     for (j = 0; j <= number-i; j++)
     {
       cout << " " ;
     }
     k=0;
     while (k != (2*i-1))
     {
       if (k == 0 || k == 2*i-2)
       cout << "*";
       else
       cout << " ";
       k++;
     }
     cout << endl;
    }
  return 0;
}