#include<iostream>              
using namespace std;

class fahrenheit{  
    private:
        float t;
    public:
       float toCel(float t=0){
           float c;
           c=(t-32.0)*5.0/9.0;
           return c;
       }
};

class celcius{  
    private:
        float t;
    public:
       float toFah(float t=0){
           float f;
           f=(t*9.0/5.0)+32.0;
           return f;
       }
};



int main()
{
    float f, c, newfah, newcel;
    cout<<"Enter the temperature in fahrenheit : "<<endl;
    cin>>f;
    fahrenheit feh;
    newfah=feh.toCel(f);
    cout<<"After converse to celcius temperature is : "<<newfah<<endl;

    cout<<"Enter the temperature in celcius : "<<endl;
    cin>>c;
    celcius cel;
    newcel=cel.toFah(c);
    cout<<"After converse to fahrenheit temperature is : "<<newcel<<endl;
    
    

    return 0;
}
