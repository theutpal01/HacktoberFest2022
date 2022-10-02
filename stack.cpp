#include<iostream>
#include<stack>
using namespace std;
class Stack
{
	public:
		int *arr;
		int top;
		int size;
		//behaviour
		//constructor
		Stack(int size)
		{
			this -> size = size; //size 
			arr = new int[size]; //dynamic array
			top = -1; 
		}
		void push(int element)
		{
			if(size - top > 1)
			{
				top++;
				arr[top] = element;
			}
			else
			{
				cout<<"stack overflow";
			}
		}
		void pop()
		{
			if(top >= 0 )
			{
				top--;
			}
			else
			{
				cout<< "Stack Underflow";
				
			}
		}
		int peek()
		{
			if(top>=0)
			{
					return arr[top];
			}
		
			else
			{
				cout<<"stack is empty";
				return -1;
			}
		}
		bool isEmpty()
		{
			if(top==-1)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
};
int main()
{
	Stack st(5);
	st.push(22);
	st.push(43);
	st.pop();
	cout<<st.peek()<<endl;
}
