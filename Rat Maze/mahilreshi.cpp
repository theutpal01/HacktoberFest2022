#include<iostream>
#define N 5
using namespace std;

int maze[N][N]  =  {
   {1, 0, 0, 0, 0},
   {1, 1, 0, 1, 0},
   {0, 1, 1, 1, 0},
   {0, 0, 0, 1, 0},
   {1, 1, 1, 1, 1}
};

int sol[N][N];         
void showPath() {
   for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++)
         cout << sol[i][j] << " ";
      cout << endl;
   }
}

bool isValidPlace(int x, int y) {       
   if(x >= 0 && x < N && y >= 0 && y < N && maze[x][y] == 1)
      return true;
   return false;
}

bool solveRatMaze(int x, int y) {
   if(x == N-1 && y == N-1) {       
      sol[x][y] = 1;
      return true;
   }

   if(isValidPlace(x, y) == true) {     
      sol[x][y] = 1; 
      if (solveRatMaze(x+1, y) == true)        
         return true;
      if (solveRatMaze(x, y+1) == true)          
         return true;
      sol[x][y] = 0;         
      return false;
   }  
   return false;
}

bool findSolution() {
   if(solveRatMaze(0, 0) == false) {
      cout << "There is no path";
      return false;
   }
   showPath();
   return true;
}

int main() {
   findSolution();
}
