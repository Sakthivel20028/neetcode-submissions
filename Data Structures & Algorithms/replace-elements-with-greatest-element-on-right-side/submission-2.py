class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        
 
        for i in range(len(arr)):
            maximum_right_element = 0
            for j in range(i+1,len(arr)):
                if arr[j] > maximum_right_element:
                    maximum_right_element = max(maximum_right_element,arr[j])
            arr[i] = maximum_right_element    
        arr[len(arr)-1] = -1        

        return arr            

        