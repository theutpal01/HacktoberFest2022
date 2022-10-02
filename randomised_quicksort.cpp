#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int p,q;

void swap(int *a,int *b)

{

    int t;

    t=*a;

    *a=*b;

    *b=t;

    return;

}



void printlist(int * arr, int *h)

{

    printf("\n [ %d",arr[0]);

    for(int i=1;i<*h;i++)

    {

        printf(", %d",arr[i]);

    }

    printf(" ]\n");

}

int * randomizedpartition(int *Arr, int *f2, int *l2)

{

    int f,f1,l,*m;

    f1=*f2;

    l=*l2;

    //Choosing a Random Pivot

    f=(rand()%(l-f1 +1))+f1;

    p=Arr[f1];

    q=Arr[f];

    swap(&p,&q);

    Arr[f1]=p;

    Arr[f]=q;

    int pivot = Arr[f];

    int i = f + 1;

    int j = l;

    int v;

    do

    {

        while (Arr[i] <= pivot)

            i++;



        while (Arr[j] > pivot)

            j--;



        if (i < j)

        {//SWAP

        //swap(&Arr[i],&Arr[j]);

            v= Arr[i];

            Arr[i] = Arr[j];

            Arr[j] =v;

        }

    } while (i < j);

 //SWAP

 //swap(&Arr[f],&Arr[j]);

    v = Arr[f];

    Arr[f] = Arr[j];

    Arr[j] = v;

    m=&j;

    return m;

}



void randomizedquicksort(int*A, int *f, int *l)

{

    int *index;

    int t;

    if (*f < *l)

    {

        index = randomizedpartition(A,f,l);

        t=*index;

        t=t-1;

        randomizedquicksort(A, f, &t);

        t=t+2;

        randomizedquicksort(A, &t, l);

    }

 return ;

}



int main()

{

    int num,ch, arr[40],d=0,t;

    int *ptr;

    printf("Enter number of Elements : ");

    cin>>num;;

    for(int i=0;i<num;i++)

    {

        cin>>arr[i];

    }

    printf("Unsorted Array : ");

   printlist(arr,&num);

   printf("\n");

   do{

    printf("\nEnter  1 to Insert/change Array, 2  for Quick Sort(A), 0 to exit : ");

    scanf("%d",&ch);

printf("\n");

    if(ch==1)

    {

        printf("Enter number of Elements : ");

        scanf("%d",&num);

        for(int i=0;i<num;i++)

            arr[i]=rand() % (num*10);

        printf("Unsorted Array : ");

        printlist(arr,&num);

        printf("\n");

    }



    else if(ch==2)

    {

        t=num-1;

        ptr=&t;

     randomizedquicksort(arr,&d,ptr);

     printf("List is sorted in Ascending Order");

     printlist(arr,&num);

     printf(" Maximum is %d, Minimum is %d\n",arr[num-1],arr[0]);

    }

    }while(ch!=0);



    return 0;

}