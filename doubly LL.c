/*

EXPERIMENT NO-05

Aim-Program on doubly linked list

Name-Sharayu Mahendra Banait
Class-SE Computer
Sec-A
Roll No-04

*/

#include<stdio.h>
#include<conio.h>

struct node
{
    int data;
    struct node *next,*prev;
};
struct node *first=NULL,*last=NULL; //doubly linked list starts from null & end at null

void Insert(); //function declaration
void Delete();//function declaration
void Display();//function declaration
void Search();//function declaration
int length();//function declaration

void main()
{
    int ch;
    do
    {
        printf("\n______________________________________________________________________________\n");
        printf("\n***####@@@  Select operation  @@@####***");
        printf("\n\t1 Insert\n\t2 Delete \n\t3 Search\n\t4 Display\n\t5 Exit");
        printf("\n   Your Choice ? ");
        scanf("%d",&ch);
        printf("\n========================================================================\n");


        switch(ch)
        {
        case 1:
            Insert();//function call
            break;
        case 2:
            Delete();//function call
            break;
        case 3:
            Search();//function call
            break;
        case 4:
            Display();//function call
            break;
        case 5:
            break;
        default :
            printf("\nWrong Choice ");
        }
    }
    while(ch!=5);
    printf("\nThank You ");
} // end of main

int length()//for counting the node
{
    int c=0;//initialize with zero
    struct node *p=first;
    if(first==NULL)
        return 0;
    else
    {
        do
        {
            c++;//increment with one
            p=p->next;//next node
        }
        while(p!=NULL);
        return c;
    }
}// end of length

void Search()//for searching an element in linked list
{
    int item;
    struct node *p;
    if(first==NULL)
        printf("\nList Empty");
    else
    {
        printf("\nEnter the number ");
        scanf("%d",&item);
        p=first;//set p at first
        while(p!=NULL && p->data!=item)
            p=p->next;//next node
        if(p==NULL)//last of linked list
            printf("\n%d is not found ", item);
        else
            printf("\n%d is found", item);
    }
}//end of search

void Display()//for display the complete list
{
    struct node *p;
    if(first==NULL)
        printf("\n List Empty");
    else
    {
        printf("\nList is \n");
        p=first;//set p at first
        do
        {
            printf("\t%d",p->data);
            p=p->next;
        }
        while(p!=NULL);//traverse until p not equal to NULL
    }
}//end of display

void Insert()//for inserting new element
{
    struct node *p,*n;
    int i,pos;
    printf("\nEnter position ");
    scanf("%d",&pos);
    if(pos<=length()+1)//length function call
    {
        n=(struct node *)malloc(sizeof(struct node));//memory allocation
        printf("\nEnter number ");
        scanf("%d",&n->data);
        if(pos==1)//inserting element at first position only
        {
            n->next=first;
            n->prev=NULL;
            first=n;
        }
        else//inserting element at last or middle of any two elements
        {
            p=first;//set pat first
            for(i=1; i<pos-1; i++) //
                p=p->next;//next node

            n->next=p->next;//link nodes to each other
            p->next=n;

            n->prev=p;
        }
        printf("\n%d is inserted at %d position ",n->data,pos);
    }

    else
        printf("\nInvalid position");
}//end of insert

void Delete()//for deleting an element from linked list
{
    struct node *p,*n;
    int pos,i;
    if(first==NULL)
        printf("\nUNDERFLOW");
    else
    {
        printf("\nEnter the position ");
        scanf("%d",&pos);
        if(pos<=length())
        {
            if(pos==1)//deleting node from first position only
            {
                n=first;//set n at deleting  node
                first=first->next;
                first->prev=NULL;//now new first node formed
                printf("\n%d is deleted from %d position", n->data,pos);
                free(n);//memory deallocation of old first
            }
            else
            {
                p=first;//deleting element at last or middle of any two elements
                for(i=1; i<pos-1; i++)
                    p=p->next;//next node

                 n=p->next;;//set n at deleting  node


                p->next = n->next;
                n->prev=p;
                printf("\n%d is deleted from %d position", n->data,pos);
                free(n);//memory deallocation
            }
        }
        else
            printf("\nInvalid position");
    }
} //end of Delete

//end of doubly linked list //

