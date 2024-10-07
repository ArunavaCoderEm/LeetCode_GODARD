class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        max_words = -69

        for i in sentences:
            split_sen = i.split(" ")
            n = len(split_sen)

            max_words = max(max_words, n)

        return max_words