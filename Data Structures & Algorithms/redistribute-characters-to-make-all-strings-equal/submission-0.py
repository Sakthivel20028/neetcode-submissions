class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        frequency_counter = defaultdict(int)
        n = len(words)

        for word in words:
            for char in word:
                frequency_counter[char] += 1


        for count in frequency_counter.values():
            if count % n !=0:
                return False

        return True                


        