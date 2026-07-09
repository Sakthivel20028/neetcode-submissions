public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int[] result = new int[arr.Length];
        for(int i = 0 ; i < arr.Length; i++)
        {
           int maxRight = -1; 
           for(int j = i+1 ; j < arr.Length ; j++)
           {
            maxRight = Math.Max(maxRight,arr[j]);
           }
           result[i] = maxRight;
        }
        result[arr.Length - 1] = -1;
        return result;
    }
}