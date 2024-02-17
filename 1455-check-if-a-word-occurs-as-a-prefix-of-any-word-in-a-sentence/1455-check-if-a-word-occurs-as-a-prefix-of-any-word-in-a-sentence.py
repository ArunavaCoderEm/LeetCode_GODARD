class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res = sentence.split()
        for i in range(0,len(res)):
            if(res[i].startswith(searchWord)): return i+1
        return -1