#include<stdio.h>
#include<conio.h>

void main()
{
	int i,j,num;
	printf("Enter the number of rows : ");
	scanf("%d",&num);
	printf("\nPyramid of * with %d rows:\n",num);
	for(i=1;i<=num;i++)
	{
		printf("\n");
		for(j=0;j<num-i;j++)
		printf(" ");
		for(j=0;j<2*i-1;j++)
		printf("*");
	}
	getch();
}