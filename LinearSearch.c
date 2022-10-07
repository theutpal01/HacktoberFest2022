#include<stdio.h>
int input(int list[],int num,int key);
void display(int list[],int num);
void linearSearch(int list[],int num,int key);
int i,flag=0;
 void main()
 {
     int num,key,list[10];
     num= input(list,num,key);
     printf("entered list is as follows:\n");
     display(list,num);
     printf("enter the key: ");
     scanf("%d",&key);
     linearSearch(list,num,key);

 }
 int input(int list[],int num,int key)
 {
     int i,n;
      printf("enter the number of elements: ");
      scanf("%d",&num);
     printf("enter the numbers\n");

       for(i=0;i<num;i++)
       {
           scanf("%d",&list[i]);
       }


       return num;
 }
 void display(int list[],int num)
 {
     int i;
     for(i=0;i<num;i++)
     {
         printf("%d\t",list[i]);
     }
     printf("\n");
 }
 void linearSearch(int list[],int num,int key)
 {
    for(i=0;i<num;i++)
     {
         if(list[i]==key)
         {
             flag=1;
             printf("Search successful!!\n key found at %d th position",i+1);
             break;

         }
     }
     if(flag==0)
        printf("search unsuccessful!!?");
 }
