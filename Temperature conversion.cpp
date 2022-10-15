#include<iostream>
using namespace std;
int main(){
	int fah, cel;
	cout<<"Enetr temperature in fahrenheit: ";
	cin>>fah;
	cel= ((fah-32)*5)/9;
	cout<<"Temperature in Celsius: "<<cel;
	return 0;
}
