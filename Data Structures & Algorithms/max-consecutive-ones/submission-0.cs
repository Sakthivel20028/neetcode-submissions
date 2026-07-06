public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int length = nums.Length;
        int count = 0;
        int maxCount = 0;
        for(int i = 0 ; i < length ; i++)
        {
            if(nums[i] == 1)
            {
                count+=1;
            }
            else
            {
                count = 0;
            }
            if(count > maxCount) maxCount = count;
        }
        return maxCount;
    }
}