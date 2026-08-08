class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hash_set = set(allowed) # We can initialize the set directly like this!
        res = 0

        for word in words:
            is_consistent = True # Reset the flag for each new word
            
            for char in word:
                if char not in hash_set:
                    is_consistent = False # Flag it as inconsistent
                    break                 # Stop checking this word
            
            # Only add to our result if the flag never changed to False
            if is_consistent:
                res += 1

        return res