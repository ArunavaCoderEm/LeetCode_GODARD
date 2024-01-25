class Solution:
    def alternateDigitSum(self, n: int) -> int:
        x,res = str(n),[]
        for i in range (len(x)):
            res.append(((-1)**(i))*int(x[i]))
        return sum(res)       