class Solution(object):
    def plusOne(self, digits):
        summ = 0
        for i in range (len(digits)):
            summ = (10*summ) + digits[i]
        res = []
        summm = str(summ + 1)
        for j in range (len(summm)):
            res.append(int(summm[j]))
        return res
        