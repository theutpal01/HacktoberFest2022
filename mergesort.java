public class mergesort{
    public static void conquer(int arr[],int si,int mid,int ei){
        int newarr[] = new int[ei-si+1];
        int indx1= si;
        int indx2=mid+1;
        int i=0;
        while(indx1<=mid && indx2<=ei){
            if(arr[indx1]<=arr[indx2]){
                newarr[i++] = arr[indx1++];
            }else{
                newarr[i++] = arr[indx2++];
            }
        }
        while(indx1<=mid){
            newarr[i++] = arr[indx1++];
        }
        while(indx2<=ei){
            newarr[i++] = arr[indx2++];
        }
        int j=si;
        for(i=0; i<newarr.length;i++,j++){
            arr[j] = newarr[i];
        }
    }
    public static void divide(int arr[],int si, int ei){
        if(si>=ei){
            return;
        }
        int mid = si + (ei-si)/2;
        divide(arr,si,mid);
        divide(arr,mid+1,ei);
        conquer(arr,si,mid,ei);
    }
    public static void main(String[] args) {
        int arr[] = {9,5,6,7,2,3};
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
        divide(arr,0,5);
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
}