class Solution(object):
    def findTheDifference(self, s, t):
        if (len(s)> len(t)):
            for i in s:
                if (s.count(i)>t.count(i)):
                    return(i)
        if (len(t)>len(s)):
            for i in t:
                if (t.count(i)>s.count(i)):
                    return(i)
        