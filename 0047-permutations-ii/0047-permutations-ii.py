class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = list(itertools.permutations(nums,len(nums)))
        for i in ans:
            if(list(i) not in res):
                res.append(list(i))
        return res       