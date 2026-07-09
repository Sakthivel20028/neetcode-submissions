public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int[] result = new int[arr.Length];
        for(int i = 0 ; i < arr.Length - 1; i++)
        {
           int maxRight = arr[i+1]; 
           for(int j = i+1 ; j < arr.Length ; j++)
           {
            if(maxRight < arr [j]){
                maxRight = arr[j];
            }
           }
           result[i] = maxRight;
        }
        result[arr.Length - 1] = -1;
        return result;
    }
}