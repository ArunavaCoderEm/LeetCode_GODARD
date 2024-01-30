class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        c = Counter(nums)
        for i,j in c.items():
            if(c[i - 1] == 0 and c[i+1] == 0 and j == 1):
                res.append(i)
        return res
