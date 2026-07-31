class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hash_set = {}
        answer = 0
        if len(set(s)) == len(s):
            return -1


        for index,char in enumerate(s):
            if char in hash_set:
                answer = max(answer,index - hash_set[char] - 1)

            else:
                hash_set[char] = index    

        return answer                
 

        