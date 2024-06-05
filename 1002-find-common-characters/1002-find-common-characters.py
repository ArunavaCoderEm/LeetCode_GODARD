class Solution:
    ## Counter Hashmap
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])
        for i in range(1,len(words)):
            c1 = Counter(words[i])
            for j in c.keys():
                c[j] = min(c[j],c1[j])
        print(c)
        res = ""
        for k in c.keys():
            res += (k*c[k])
        return (list(res))