def dec_to_base(num,base): 
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base

    base_num = base_num[::-1] 
    return base_num

class Solution:
    def sumBase(self,n: int, k: int) -> int:
        x,summ = int(dec_to_base(n,k)),0
        while(x != 0):
            rem = x % 10
            summ += rem
            x //= 10
        return summ
    
        