#include "bits/stdc++.h"
using namespace std;
bool isWon(int arr[3][3]){
	if((arr[0][0]==arr[0][1]&&arr[0][1]==arr[0][2])&&arr[0][0]!=0&&arr[0][1]!=0&&arr[0][2]!=0||(arr[1][0]==arr[1][1]&&arr[1][1]==arr[1][2])&&arr[1][0]!=0&&arr[1][1]!=0&&arr[1][2]!=0||(arr[2][0]==arr[2][1]&&arr[2][1]==arr[2][2])&&arr[2][0]!=0&&arr[2][1]!=0&&arr[2][2]!=0)
		return true;
	if((arr[0][0]==arr[1][0]&&arr[1][0]==arr[2][0])&&arr[0][0]!=0&&arr[1][0]!=0&&arr[2][0]!=0||(arr[0][1]==arr[1][1]&&arr[1][1]==arr[2][1])&&arr[0][1]!=0&&arr[1][1]!=0&&arr[2][1]!=0||(arr[0][2]==arr[1][2]&&arr[1][2]==arr[2][2])&&arr[0][2]!=0&&arr[1][2]!=0&&arr[2][2]!=0)
		return true;
	if((arr[0][0]==arr[1][1]==arr[2][2])&&arr[0][0]!=0&&arr[1][1]!=0&&arr[2][2]!=0||(arr[0][2]==arr[1][1]&&arr[1][1]==arr[2][0])&&arr[0][2]!=0&&arr[1][1]!=0&&arr[2][0]!=0)
		return true;	
	return false;
}
bool isTie(int arr[3][3]){
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			if(arr[i][j]==0)return false;
		}
	}
	return true;
}
int main(){
	// #ifndef ONLINE_JUDGE
	// freopen("input.txt","r",stdin);
	// freopen("output.txt","w",stdout);
	// #endif
	label:
	cout<<"NOTE: 0 based indexing"<<endl; 
	cout<<"Press y to play game and n to end the game"<<endl;
	char x;
	cin>>x;
	//cout<<x<<endl;
	if(x=='y'){
		int arr[][3] ={
					{0,0,0},
					{0,0,0},
					{0,0,0}
					};
		for(int i=0;i<3;i++){
				cout<<"|";
				for(int j=0;j<3;j++){
					if(arr[i][j]==0){
						cout<<" ";
					}
					if(arr[i][j]==1){
						cout<<"x";
					}
					if(arr[i][j]==2){
						cout<<"o";
					}
					cout<<"|";
				}
				cout<<endl;
			}
		while(true){
			cout<<"Waiting for player 1"<<endl;
		joe:int x,y;
			cin>>x>>y;
			if(arr[x][y]==0)
				arr[x][y] = 1;
			else
				{
					cout<<"You noob. Don't mark existing square. Choose again"<<endl;
					goto joe;
				}
			for(int i=0;i<3;i++){
				cout<<"|";
				for(int j=0;j<3;j++){
					if(arr[i][j]==0){
						cout<<" ";
					}
					if(arr[i][j]==1){
						cout<<"x";
					}
					if(arr[i][j]==2){
						cout<<"o";
					}
					cout<<"|";
				}
				cout<<endl;
			}
			if(isWon(arr)){
				cout<<"Player 1 wins"<<endl;
						break;	}
			if(isTie(arr)){
				cout<<"The game is Tied"<<endl;
				break;
			}
			cout<<"Waiting for player 2"<<endl;
			joe2:int a,b;
			cin>>a>>b;
			if(arr[a][b]==0)
				arr[a][b] = 2;
			else
				{
					cout<<"You noob. Don't mark existing square. Choose again"<<endl;
					goto joe2;
				}
			for(int i=0;i<3;i++){
				cout<<"|";
				for(int j=0;j<3;j++){
					if(arr[i][j]==0){
						cout<<" ";
					}
					if(arr[i][j]==1){
						cout<<"x";
					}
					if(arr[i][j]==2){
						cout<<"o";
					}
					cout<<"|";
				}
				cout<<endl;
			}
			if(isWon(arr)){
				cout<<"Player 2 wins"<<endl;
				break;
			}
			if(isTie(arr)){
				cout<<"The game is Tied"<<endl;
				break;
			}
		}
		
	} 
	else {
		cout<<"The game is over"<<endl;
	}
	cout<<"Press 1 to play again"<<endl;
		int j;
		cin>>j;
		if(j==1)
			goto label;
	return 0;
}

