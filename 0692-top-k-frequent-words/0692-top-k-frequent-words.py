class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = sorted(Counter(words).items(), key = lambda ard: (-ard[1], ard[0]))
        res = c[0:k]
        t = dict(res)
        return [x for x in (t.keys())]