class Solution(object):
    def addDigits(self, num):
        if (len(str(num)) == 1):
            return num
        while (len(str(num)) != 1):
            sum = 0
            for i in (str(num)):
                sum += (int(i))
            num = sum
        return sum 
        