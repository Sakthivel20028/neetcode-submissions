class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        res = [-1] * len(nums1)

        for index,nums in enumerate(nums1):
            hash_map[nums] = index

        for i in range(len(nums2)):
            if nums2[i] not in hash_map:
                continue
            for j in range(i+1,len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = hash_map[nums2[i]]
                    res[idx] = nums2[j] 
                    break;
        return res                 


            


        