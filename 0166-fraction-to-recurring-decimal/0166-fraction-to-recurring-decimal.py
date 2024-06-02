class Solution:
    # Mighnt get TLE for BrFor ok not tle but not good
    def fractionToDecimal(self, num: int, den: int) -> str:
        if (num % den == 0):
            return str(num // den)    
        res = []
        if(num < 0 and den > 0) : res.append('-')
        elif(num > 0 and den < 0): res.append('-')
        num, den = abs(num), abs(den)
        k = num // den
        res.append(str(k))
        res.append('.')
        rem = num % den
        bfp = []
        rems = []  
        while (rem != 0):
            if (rem in rems):
                repeat_index = rems.index(rem)
                bfp.insert(repeat_index, '(')
                bfp.append(')')
                break       
            rems.append(rem)
            rem *= 10
            bfp.append(str(rem // den))
            rem %= den    
        res.extend(bfp)
        return ''.join(res)
        