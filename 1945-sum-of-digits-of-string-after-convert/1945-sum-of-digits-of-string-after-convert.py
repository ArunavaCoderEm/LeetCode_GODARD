import string
class Solution:
    def getLucky(self,s: str, k: int) -> int:
        summ = 0
        for i in s:
            x = 1 + string.ascii_lowercase.index(i)
            s = s.replace(i,str(x))
        temp = int(s)
        while (k > 0):
            for j in range(len(str(temp))):
                rem = temp % 10
                summ += rem
                temp //= 10
            temp = summ
            summ = 0
            k -= 1
        return temp