package com.chirag;

import java.util.Arrays;
//max element pakdo and last me bhejdo, then length-1 pe loop iterate karo
// O(n^2) avg and best
public class SelectionSort {
    public static int greatest(int[] arr, int end)
    {
        int max = 0;
        for (int i = 0; i <=end; i++) {
            if(arr[i] > arr[max])
            {
                max = i;
            }
        }
        return max;
    }
    public static void main(String[] args) {
        int[] arr = {0 ,5, -32 , 4};
        for (int i = arr.length-1; i >= 0; i--) {
            int max = greatest(arr, i);
            int temp = arr[max];
            arr[max] = arr[i];
            arr[i] = temp;
        }
        System.out.println(Arrays.toString(arr));
    }
}
// 1 2 3 4 6 7 9  10