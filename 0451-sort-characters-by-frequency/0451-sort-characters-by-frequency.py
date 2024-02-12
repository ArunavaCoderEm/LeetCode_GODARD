class Solution:
    def frequencySort(self, s: str) -> str:
        res = ''
        c = Counter(s)
        while(len(res) != len(s)):
            for i,j in list(c.items()):
                if(j == max(c.values())):
                    res += str(j*i)
                    del c[i]
        return res