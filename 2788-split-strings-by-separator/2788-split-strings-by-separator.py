class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for i in words:
            ans = i.split(separator)
            for j in ans: res.append(j)
        res = list(filter(None, res))
        return res
