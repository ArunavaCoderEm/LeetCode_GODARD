# 4 from my pendings


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stk = [num[0]]
        i = 1        
        
        
        while (i < len(num)):
            while (k > 0):
                if (len(stk) and stk[-1] > num[i]):
                    k -= 1
                    stk.pop()
                else: break
            stk.append(num[i])
            i += 1
            
        while (k > 0):
            stk.pop()
            k -= 1

        while (len(stk) and stk[0] == "0"): stk.pop(0)
            
        retres = ""

        retres = "".join(stk)
        
        return "0" if (retres == "") else retres