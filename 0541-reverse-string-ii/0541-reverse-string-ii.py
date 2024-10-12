class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        j = i + k
        n = len(s)
        while (i < n):
            s = s[:i] + s[i:j][::-1] + s[j:]
            i += 2*k
            j = i + k
        return s