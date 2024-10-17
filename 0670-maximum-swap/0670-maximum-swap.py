## WTF just happened to me ?? 
## HTF everything today working out for me ??
## Fixed every error on Q-Filer efficiently 
## PostgreSQL working properly 

## Connected all frontend with backend very properly and efficiently

## And now this fucking LC with 100 % ?? What ??????


class Solution:
    def maximumSwap(self, num: int) -> int:
        res = list(map(int, list(str(num))))
        i, j = 0, len(res) - 1
        maxoutofit = sorted(res, reverse = True)
        if (res == maxoutofit): return num
        while (res[i] == maxoutofit[i]):
            i += 1
        max_digit = maxoutofit[i]
        j = len(res) - 1
        while (res[j] != max_digit):
            j -= 1
        res[i], res[j] = res[j], res[i]   
        summ = 0
        for i in res: summ = (10 * summ) + i

        return summ  
            