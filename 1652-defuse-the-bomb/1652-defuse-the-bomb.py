class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        ## cyclic sub array easy (CYCLIC INCREMENT X = (X + 1) % LEN) 
        if(k == 0): return [0]*len(code)
        if(k > 0):
            for i in range(len(code)):
                summ = 0
                for j in range(1,k+1):
                    summ += code[(i + j) % len(code)]
                res.append(summ)
        else:
            for i in range(len(code)):
                summ = 0
                for j in range(1,abs(k)+1):
                    summ += code[(i - j) + len(code) % len(code)]
                res.append(summ)         
        return res