class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            alph = [0] * 26
            for c in i:
                alph[ord(c) - ord('a')] += 1
            res[tuple(alph)].append(i)
        return res.values()
