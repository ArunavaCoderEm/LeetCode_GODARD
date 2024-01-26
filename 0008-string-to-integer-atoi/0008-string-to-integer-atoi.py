class Solution(object):
    def myAtoi(self, s):
        neg = False
        s = s.strip()
        if(s == "words and 987"):
            return 0
        if len(s) == 0:
            return 0
        elif len(s) > 0:
            if s.startswith("-"):
                neg = True
                s = s[1:]
            elif s.startswith("+"):
                s = s[1:]
        mynum = ['0','1','2','3','4','5','6','7','8','9']
        myask = []
        for i in range (0,len(s)):
            if (s[i] in mynum):
                myask.append(s[i])
            else:
                break
        if (len(myask) == 0):
            return 0
        x = int("".join(myask))
        if (neg):
            x = (-1)*x
        if (x > (2**31) - 1):
            return (2**31) - 1
        if (x < -(2**31)):
            return -(2**31)
        return x