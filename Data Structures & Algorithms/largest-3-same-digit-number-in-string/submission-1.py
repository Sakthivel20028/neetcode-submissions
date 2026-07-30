class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in "9876543210":
            substring = digit * 3
            if substring in num:
                return substring
        return ""        
        


        