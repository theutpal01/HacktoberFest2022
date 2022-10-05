#include <iostream>
using namespace std;
//root -> next 
//temp
class node{ 
public:
int data;
node *next;
node (int data){
this->data =data;
next = NULL;
}
};
//insertion
node *isertnode(node *head , int i,int data){ 
node *newnode = new node(data);
if(head == NULL){
return head;
}
if(i==1){
newnode->next =head;
head= newnode;
return head;
}
node *a=isertnode(head->next ,i-1 ,data);
head->next= a;
}
//taking input to form node 
node *takeinput (){ 
int data;
cin>>data;
node *head =NULL;
node *tail =NULL;
while(data!= -1){
node *newnode = new node(data);
if(head == NULL){
head=newnode;
tail =newnode;
}
else{
tail->next =newnode;
tail = tail->next;
}
cin>>data;
}
return head;
}
//print
void print(node *head){ 
while (head !=NULL){
cout<<head->data<<" ";
head = head->next;
}
cout<<endl;
}
//run and run2 for deletion work 
node *run(node *head ,int i){ 
int count =0;
node *temp =head;
int j=i-1;
if(j==0){
head=head->next;
return head;
}
while (temp !=NULL && count<j-1){
temp=temp->next;
count++;
}
if(temp !=NULL){
node *a =temp->next;
node *b=a->next;
temp->next =b;
delete a;
}
return head;
}
node *run2(node *head ,int i){ 
if(head ==NULL){
return head;
}
if(i== 0){
head =head->next;
return head;
}
node *b=run2(head->next ,i-1);
head->next=b;
}
//for searching 
void search(node *head){
node *temp=head;
int j;
int i=1;
cout<<"Enter the searching element"<<endl;
cin>>j;
while(temp != NULL){
if(temp -> data == j){
cout<<temp->data << " at position "<< i << endl;
break;
}
else{
temp = temp -> next;
i++; 
}
if(temp == NULL){
cout<<"Element not found"<< endl;
}
}
}
//input for the user 
int main(){
cout<<"Enter the numbers you want in array , type -1 to exit = "<<endl;
node *head =takeinput();
print(head);
cout<<endl;
int c;
cout<<"\nEnter 0 for more itration"<<endl;
cin>>c;
while(c== 0){
int p;
cout<<"-------------------"<<endl;
cout<<"1. for Delation"<<endl;
cout<<"2. for Insertion"<<endl;
cout<<"3. for Searching"<<endl;
cout<<"-------------------"<<endl;
cin>>p;
if(p==1){
int i;
cout<<"\nEnter the position for deletion : "<<endl;
cin>>i;
head =run(head,i);
print(head);
}
if(p==2){
int j, data;
cout<<"\nEnter the position and data for insertion : "<<endl;
cin>>j>>data;
head=isertnode(head,j,data);
print(head);
}
cout<<"\nEnter 1 to exit \nEnter 0 for more operations to work\n "<<endl;
cin>>c;
if(p==3){
search(head);
}
}
return 0;
}