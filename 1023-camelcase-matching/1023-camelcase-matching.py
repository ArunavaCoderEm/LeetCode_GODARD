# had to take hint and watch YT

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        chklist = []
        for i in queries:
            count = 0
            for j in range(len(i)):
                if (count < len(pattern) and i[j] == pattern[count]): count += 1
                elif (i[j] >= "A" and i[j] <= "Z"): 
                    chklist.append(False)
                    break
                if (j == len(i) - 1):
                    if(count == len(pattern)):
                        chklist.append(True)
                    else :
                        chklist.append(False)
        return chklist
