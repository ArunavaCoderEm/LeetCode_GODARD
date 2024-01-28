class Solution:
    def secondHighest(self, s: str) -> int:
        res = []
        cha = ['1','2','3','4','5','6','7','8','9','0']
        for i in s:
            if(i in cha):
                res.append(int(i))
        res = sorted(list(set(res)))
        if(len(res) == 1 or len(res) == 0):
            return -1
        return res[len(res)-2]