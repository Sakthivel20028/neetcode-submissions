class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_list = {}
        for num in nums:
            if num in unique_list:
                return True
            else:
                unique_list[num] = num
        return False            
        