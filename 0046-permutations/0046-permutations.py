class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list(itertools.permutations(nums,len(nums)))
        res = [list(i) for i in ans]
        return res