class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            res = haystack.index(needle)
        except:
            res = -1
        return res