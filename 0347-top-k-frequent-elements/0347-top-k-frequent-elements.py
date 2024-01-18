def gets(d, val):
    for k,v in d.items():
        if (v == val):
            return k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = (Counter(nums))
        res = []
        for i in range(k):
            x = max(c.values())
            p = gets(c,x)
            res.append(p)
            del c[p]
        return res