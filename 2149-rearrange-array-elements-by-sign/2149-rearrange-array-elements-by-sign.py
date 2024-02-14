class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [i for i in nums if(i > 0)]
        neg = [j for j in nums if(j < 0)]
        k,p,n = 0,0,0
        res = []
        while (k < len(nums)):
            if(k % 2 == 0):
                res.append(pos[p])
                p += 1
            else:
                res.append(neg[n])
                n += 1
            k += 1
        return res