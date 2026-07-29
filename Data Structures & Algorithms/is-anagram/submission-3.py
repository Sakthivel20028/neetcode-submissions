class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = defaultdict(int)
        dict_2 = defaultdict(int)
        if len(s) != len(t):
            return False

        for char in s:
            dict_1[char] +=1 

        for char in t:
            dict_2[char] +=1


        if dict_1 == dict_2:
            return True
        else:
            return False            


        