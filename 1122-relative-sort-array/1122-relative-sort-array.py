class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        res = []
        for i in arr2:
            res += [i]*c[i]
            del c[i]
        resi = sorted(c)
        for j in resi:
            res += [j] * c[j]
        return res