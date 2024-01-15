class Solution(object):
    def subtractProductAndSum(self, n):
        sum,mul = 0,1
        for i in str(n):
            sum += int(i)
            mul *= int(i)
        return (mul-sum)
            