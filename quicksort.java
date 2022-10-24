import java.util.Scanner;
import java.util.Random;
public class quicksort {
	static final int MAX= 10005;
	static int[] a=new int[MAX];
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		System.out.println("Enter the number of elements");
		int n=input.nextInt();
		Random random=new Random();
		System.out.println("Enter the array elements");
		for(int i=0;i<n;i++)
			a[i]=input.nextInt();
			//a[i]=random.nextInt(10000);
			Quicksort(0,n-1);
		long startTime = System.nanoTime();
		Quicksort(0,n-1);
		long stopTime = System.nanoTime();
		long elapsedTime = stopTime-startTime;
		System.out.println("time elapsed for "+n+ " elements in ms: "+(double)elapsedTime/1000000);
		System.out.println("The sorted array elements:");
		for(int i=0;i<n;i++)
			System.out.print(a[i]+" ");
		input.close();
		
	}
	public static void Quicksort(int p, int r)
	{
		int i,j,temp;
		if(p<r)
		{
			i=p;
			j=r+1;
			int pivot =a[p];
			while(true)
			{
				i++;
				while(a[i]<pivot && i<r)
					i++;
				j--;
				while(a[j]>pivot)
					j--;
				if(i<j)
				{
					temp=a[i];
					a[i]=a[j];
					a[j]=temp;
				}else
					break;
				
			}
			a[p]=a[j];
			a[j]=pivot;
			Quicksort(p,j-1);
			Quicksort(j+1,r);
		}
	}
}
