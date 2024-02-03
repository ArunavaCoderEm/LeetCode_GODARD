class Solution(object):
    def isValid(self, s):
        stk = ['0']
        if (len(s) == 1):
            return False
        f,se,t = 0,0,0
        for i in s:
            if (i == '('):
                stk.append(i)
                f += 1
            if (i == ')'):
                f -= 1
                check = stk.pop()
                if (check + i != '()'):
                    return False
            if (i == '{'):
                stk.append(i)
                se += 1
            if (i == '}'):
                se -= 1
                check = stk.pop()
                if (check + i != '{}'):
                    return False
            if (i == '['):
                stk.append(i)
                t += 1
            if (i == ']'):
                t -= 1
                check = stk.pop()
                if (check + i != '[]'):
                    return False               
        return (f == 0 and se == 0 and t == 0)