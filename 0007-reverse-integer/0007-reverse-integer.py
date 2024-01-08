class Solution(object):
    def reverse(self,x):
        e = int(str(x)[::-1].replace("-",""))
        if (e <= ((2**31)-1)):
            if (x > 0):
                return int(str(x)[::-1])
            else :
                z = str(x).replace("-","")
                m = z[::-1]
                return -(int(m))
        else:
            return 0
