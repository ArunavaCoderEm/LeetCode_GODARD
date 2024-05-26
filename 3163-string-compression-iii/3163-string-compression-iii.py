class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1
        while(len(word) > 1):
            for i in range(1,len(word)):
                if(word[i] == word[i-1] and i < 9): count += 1
                else: 
                    print(count)
                    comp += f"{count}{word[i-1]}"
                    count = 1
                    break
            word = word[i:len(word)]
        comp += f"{count}{word[0]}"
        return comp