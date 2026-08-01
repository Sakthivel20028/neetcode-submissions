class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        frequency_count = defaultdict(int)
        
        for num in nums:
            frequency_count[num] += 1
            if frequency_count[num] > 1:
                return num
        