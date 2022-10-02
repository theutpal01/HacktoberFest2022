#include<iostream>

using namespace std;

int main()
{
    int data[1][8][8] = {
        {
            { 1,1,1,1,1,1,1,1 },
            { 1,1,1,0,0,1,1,1 },
            { 1,1,1,0,0,1,1,1 },
            { 1,1,1,1,1,1,1,1 },
            { 1,1,1,1,1,1,1,1 },
            { 1,1,1,1,1,1,0,1 },
            { 1,1,1,1,1,1,1,1 },
            { 1,1,1,1,1,1,1,1 }
        }
    };
    int i, j, k;

    cout<<"Membuat bentuk pintu menggunakan array 3 dimensi"<<endl;
    cout<<endl;

    for(i = 0; i < 1; i++){
        for(j = 0; j < 8; j++){
            for(k = 0; k < 8; k++){
                if(data[i][j][k] == 1){
                    cout<<'\xDB';
                } else {
                    cout<<'\x20';
                }
            }
            cout<<endl;
        }
    }

    return 0;
}
