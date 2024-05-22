class Solution:
    def clumsy(self, n: int) -> int:
        strcalc = ""
        op = 1
        for i in range(0,n):
            if(op == 1):
                strcalc += str(n - i) + '*'
                op += 1
            elif(op == 2):
                strcalc += str(n - i) + '//'
                op += 1
            elif(op == 3):
                strcalc += str(n - i) + '+'
                op += 1
            else:
                strcalc += str(n - i) + '-'
                op = 1
        if(not strcalc[-1].isdigit()):
            if(strcalc.endswith('//')):
                strcalc = (strcalc[0:len(strcalc) - 2])
            else: 
                strcalc = (strcalc[0:len(strcalc) - 1])  
        res = eval(strcalc)
        return int(res)