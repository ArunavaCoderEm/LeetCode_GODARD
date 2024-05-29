def commul(n1,n2):
    return n1 * n2
## I don't know why it took 20 mins to solve LOL
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        x1 = 0
        i = 0
        x2 = 0
        fl1 = True
        fll = True
        fl = True
        if('+' in num1 or '+-' in num1):
            if(num1[i] == '-'): 
                i += 1
                fll = False
            while(num1[i] != '+'):
                x1 = 10*x1 + int(num1[i])
                i += 1
            i += 1
            if(not fll): x1 = (-1) * x1
            if(num1[i] == '-'): 
                i += 1
                fl1 = False
        while(num1[i] != 'i'):
            x2 = 10*x2 + int(num1[i])
            i += 1
        if(not fl1): x2 = (-1) * x2
        y1 = 0
        j = 0
        y2 = 0
        fl2 = True
        if('+' in num2 or '-' in num2):
            while(num2[j] != '+'):
                if(num2[j] == '-'): 
                    j += 1
                    fl = False
                y1 = 10*y1 + int(num2[j])
                j += 1
            j += 1
            if(not fl): y1 = (-1) * y1
            if(num2[j] == '-'): 
                j += 1
                fl2 = False
        while(num2[j] != 'i'):
            y2 = 10*y2 + int(num2[j])
            j += 1
        if(not fl2): y2 = (-1) * y2
        print(x1,x2,y1,y2)
        re = (x1*y1) - (x2*y2)
        img = (x1*y2) + (y1*x2)
        res = f"{re}+{img}i"
        print(res)
        return res