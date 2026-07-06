public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int length = nums.Length;
        int position = 0;
        for(int i = 0 ; i <length ; i++)
        {
            if(nums[i] != val)
            {
                nums[position] = nums[i];
                position++;
            }
        }
        return position;
    }
}