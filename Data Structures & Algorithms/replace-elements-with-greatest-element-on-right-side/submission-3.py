class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        
 
        for i in range(len(arr)):
            maximum_right_element = 0
            for j in range(i+1,len(arr)):
                maximum_right_element = max(arr[j],maximum_right_element)
            arr[i] = maximum_right_element    
        arr[len(arr)-1] = -1        

        return arr            

        