class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_map = {}
        output = []

        for index,num in enumerate(nums):
            hash_map[num] = index


        for i in range(1,len(nums)+1):
            if i not in hash_map:
                output.append(i)

        return output                

        