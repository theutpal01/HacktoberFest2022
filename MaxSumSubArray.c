#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

typedef struct resArr{
    int lm;
    int rm;
    int s;
}resA;

 resA* Find_Max_Crossing_Subarray(int*arr,int low,int mid ,int high){
        resA*p=(resA*)malloc(sizeof(resA));
        int leftsum=(INT_MIN);
        int rightsum=(INT_MIN);
        int sum=0;
        for(int i=mid;i>=low;i--){
            sum=sum+arr[i];
            if(sum>leftsum){
                leftsum=sum;
                p->lm=i;
            }
        }
        sum=0;
        for(int j=mid+1;j<=high;j++){
            sum=sum+arr[j];
            if(sum>rightsum){
                rightsum=sum;
                p->rm=j;
            }
        }
        p->s=leftsum+rightsum;
        return p;
}

resA* Find_Max_Subarray(int*arr,int low,int high){
    resA*p=(resA*)malloc(sizeof(resA));
    if(low==high){
            p->lm=low;
            p->rm=high;
            p->s=arr[low];
    }else
    {
        int mid=(low+high)/2;
        resA *temp1,*temp2,*temp3;
        temp1=Find_Max_Subarray(arr,low,mid);
        temp2=Find_Max_Subarray(arr,mid+1,high);
        temp3=Find_Max_Crossing_Subarray(arr,low,mid,high);
        if((temp1->s)>=(temp2->s)&&(temp1->s)>=(temp3->s)){
            p=temp1;
        }else if((temp2->s)>=(temp1->s)&&(temp2->s)>=(temp3->s)){
            p=temp2;
        }else{
            p=temp3;
        }
        return p;
    }
    
    
}
int main(){
    
    return 0;
}
