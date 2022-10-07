import java.util.Scanner;

public class sorting {
    public static void printArray(int arr[]){
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i] + " ");
        }
    }

    public static void  bubbleSort(int arr[]){
        for(int i=0;i<arr.length-1;i++){
            for(int j=0;j<arr.length-1-i;j++){
                if(arr[j]>arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    public static void selectionSort(int arr[]){
        for(int i=0;i<arr.length-1;i++){
            int smallest = i;
            for(int j=i+1;j<arr.length;j++){
                if(arr[smallest]>arr[j]){
                    smallest = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[smallest];
            arr[smallest] = temp;
        }
    }

    public static void insertionSort(int arr[]){
        for(int i=1;i<arr.length;i++){
            int smallest = arr[i];
            int j=i-1;
            while(j>=0 && smallest<arr[j]){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = smallest;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the no. of values u want to enter in the array");
        int n = sc.nextInt();
        int arr[]  = new int[n]; 
        for(int i=0;i<arr.length;i++){
            n = sc.nextInt();
            arr[i] = n;
        }
        
        System.out.println(arr.length);
        
        // bubbleSort(arr);
        // selectionSort(arr);
        insertionSort(arr);
        printArray(arr);
        
    }
}
