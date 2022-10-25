/*Life is onetime offer ,use it well*/
#include<bits/stdc++.h>
using namespace std;
//Calculating a^b%MOD using binaryExponentiation
const int MOD = 1e9 + 7;
#define int long long
int powExpo(int a, int n, int MOD)
{
  int result = 1;
  while (n > 0)
  {
    if (n & 1)
    {
      result *= a % MOD;
      result = ((result % MOD) + MOD) % MOD;
    }

    a *= a % MOD;
    //handling negative modulo
    a = ((a % MOD) + MOD) % MOD;
    n = n >> 1;
  }
  return result;

}

int32_t main()
{
  int a = 2, n = 40 ;
  cout << powExpo(a, n, MOD) << endl;

  return 0;
}
