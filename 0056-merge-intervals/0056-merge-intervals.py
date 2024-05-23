## 7 wrong submissions before to do this !! NICE 

def first(a):
    return a[0]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = sorted(intervals, key=first)
        anss = [res[0]]
        if(len(intervals) == 1): return intervals
        for i in range(1,len(res)+1):
            if(anss[len(anss) - 1][1] >= res[i-1][0]):
                anss[len(anss) - 1][1] = max(anss[len(anss) - 1][1], res[i-1][1])
            else:
                anss.append(res[i-1])
        return anss