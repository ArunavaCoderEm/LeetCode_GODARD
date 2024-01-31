class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = []
        c = Counter(arr)
        for i,j in c.items():
            if(i == j):
                res.append(i)
        if(len(res) > 0):
            return max(res)
        return -1