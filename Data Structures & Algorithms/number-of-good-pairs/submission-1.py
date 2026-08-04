class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        good_pair = 0
        for num in nums:
            if num not in hash_map:
                hash_map[num] +=1

            else:
                good_pair += hash_map[num]
                hash_map[num] +=1

        return good_pair                              