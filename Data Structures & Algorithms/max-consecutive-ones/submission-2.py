class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count_one = 0
        for num in nums:
            if num == 1:
                count_one += 1
                max_ones = max(max_ones,count_one)  
            else:
                count_one = 0

        return max_ones             


        