#include <stdio.h>
#include <stdlib.h>

int main()
{
    int number_of_elemenst = 6;
    int numbers[6] = {41,2,43,11,6,3};

    //selections sort
    for(int i=0; i<number_of_elemenst-1;i++){
        int minIndex = i;
        for(int j=i+1; j<number_of_elemenst;j++){
            if(numbers[minIndex]>numbers[j]){
                minIndex = j;
            }
        }

        if(minIndex != i){
            int temp = numbers[i];
            numbers[i] = numbers[minIndex];
            numbers[minIndex] = temp;
        }
    }

    for(int k=0; k<number_of_elemenst;k++){
        printf("%d ,", numbers[k]);
    }



    return 0;
}
