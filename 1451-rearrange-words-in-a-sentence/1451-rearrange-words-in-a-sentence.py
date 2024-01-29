class Solution:
    def arrangeWords(self, text: str) -> str:
        res = text.split()
        res = sorted(res,key=len)
        s = " ".join(res)
        return s.capitalize()        