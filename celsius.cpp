//  Program to Convert Celsius to Fahrenheit in C++ language
#include <iostream>
using namespace std;

int main(){
    float cel, fahren;

    // Taking input
    cout << "Enter the temperature in Celsius: ";
    cin >> cel;

    // Converting to  fahrenheit
    fahren = (cel * 9.0) / 5.0 + 32;

    // Print result
    cout << "The temperature in degree Fahrenheit: " << fahren << endl;

    return 0;
}
