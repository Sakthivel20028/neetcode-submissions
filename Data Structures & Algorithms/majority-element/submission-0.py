class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)

        for index,num in enumerate(nums):
            hash_map[num]  += 1


        for key,value in hash_map.items():
            if value > len(nums) / 2:
                return key         