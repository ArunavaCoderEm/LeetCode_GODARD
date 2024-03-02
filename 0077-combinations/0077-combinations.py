class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [i for i in range(1,n+1)]
        ans = list(itertools.combinations(res,k))
        ansres = [list(i) for i in ans]
        return ansres