class Solution:
    def smallestNumber(self, num: int) -> int:
        if(num == 0): return 0
        elif(num > 0):
            res = sorted(list(str(num)))
            i = 0
            c = 0
            ret = ''
            while (res[i] == '0' and i < len(res)):
                c += 1
                i += 1
            last = ''.join(res[i+1:])
            ret += f"{res[i]}{i*'0'}{last}"
        else:
            n = str(num)[1:]
            res = sorted(list(str(num)),reverse = True)
            i = 0
            c = 0
            ret = ''
            while (res[i] == '0' and i < len(res)):
                c += 1
                i += 1
            last = ''.join(res[i+1:len(res)-1])
            ret += f"-{res[i]}{i*'0'}{last}"        
        return int(ret) 