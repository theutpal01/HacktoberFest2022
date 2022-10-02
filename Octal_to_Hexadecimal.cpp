// C++ program to convert Octal
// to Hexadecimal
#include<bits/stdc++.h>
using namespace std;
 
// Function to convert octal to decimal
int octalToDecimal(int n)
{
    int num = n;
    int dec_value = 0;
     
    // Initializing base value
    // to 1, i.e 8^0
    int base = 1;
   
    int temp = num;
    while (temp)
    {
         
        // Extracting last digit
        int last_digit = temp % 10;
        temp = temp / 10;
         
        // Multiplying last digit with
        // appropriate base value and
        // adding it to dec_value
        dec_value += last_digit * base;
   
        base = base * 8;
    }
    return dec_value;
}
 
// Function to convert decimal
// to hexadecimal
string decToHexa(int n)
{
     
    // char array to store
    // hexadecimal number
    char hexaDeciNum[100];
     
    // counter for hexadecimal
    // number array
    int i = 0;
    while(n != 0)
    {   
         
        // Temporary variable to
        // store remainder
        int temp  = 0;
           
        // Storing remainder in
        // temp variable.
        temp = n % 16;
           
        // Check if temp < 10
        if (temp < 10)
        {
            hexaDeciNum[i] = temp + 48;
            i++;
        }
        else
        {
            hexaDeciNum[i] = temp + 87;
            i++;
        }
        n = n / 16;
    }
     
    string ans = "";
       
    // Printing hexadecimal number array
    // in reverse order
    for(int j = i - 1; j >= 0; j--)
    {
        ans += hexaDeciNum[j];
    }
    return ans;
}
 
// Driver Code
int main()
{
    string hexnum;
    int decnum, octnum;
     
    // Taking 5123 as an example of
    // Octal Number.
    octnum = 5123;
     
    // Convert Octal to Decimal
    decnum = octalToDecimal(octnum);
     
    // Convert Decimal to Hexadecimal
    hexnum = decToHexa(decnum);
     
    cout << "Equivalent Hexadecimal Value = "
         << hexnum << endl;
}
 
// This code is contributed by Virendra-94