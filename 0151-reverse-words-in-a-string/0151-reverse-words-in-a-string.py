class Solution(object):
    def reverseWords(self, s):
        res = s.split()
        res.reverse()
        resj = " ".join(res)
        return resj
        