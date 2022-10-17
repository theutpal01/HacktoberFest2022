public class LinearSearch {
    public static void main(String[] args) {
        int[] marks={12,43,23,54,65,76,32,89,90};
        System.out.println("This is program for linear search");
        System.out.println(lnrSrch(marks, 23));
    }
    static int lnrSrch(int[] arr, int target){
            if(arr.length==0){
                return -1;
            }

            for(int index=0; index<arr.length;index++){
                int element=arr[index];
                if(element==arr[index]){
                    return arr[index];
                }
            }
            return -1;           
        }
}
