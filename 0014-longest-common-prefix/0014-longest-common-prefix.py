class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lgp = ""
        strs = sorted(strs)
        m = strs[0]
        n = strs[len(strs) - 1]
        for i in range (len(m)):
            if(m[i] != n[i]): return lgp
            lgp += m[i]
        return lgp