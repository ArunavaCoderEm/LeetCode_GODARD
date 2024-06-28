from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = {}
        for i in roads:
            if (i[0] in d):
                d[i[0]] += 1
            else:
                d[i[0]]=1
            if (i[1] in d):
                d[i[1]] += 1
            else:
                d[i[1]] = 1
        d = sorted(d.items(), key=lambda x:x[1]) 
        res = {}
        i = 1
        while (n >= 0): 
            try:
                res[d[-i][0]] = n
                n -= 1
                i += 1 
            except:
                break           
        cnt = 0
        for i in roads: 
            cnt = cnt + res[i[0]] + res[i[1]]
        return cnt
