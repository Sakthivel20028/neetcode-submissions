class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_list = set()
        for num in nums:
            if num in unique_list:
                return True
            else:
                unique_list.add(num)
        return False            
        