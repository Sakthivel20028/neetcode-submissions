class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        found = False
        output = []
        for i in range(len(nums1)):
            found = False
            index = nums2.index(nums1[i])
            for j in range(index+1,len(nums2)):
                if nums2[index] < nums2[j]:
                    output.append(nums2[j])
                    found = True
                    break;
            if not found:
                output.append(-1)       

        return output            
            


        