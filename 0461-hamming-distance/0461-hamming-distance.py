class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x = bin(x).replace("0b","")
        y = bin(y).replace("0b","")
        if (len(x) < len(y)):
            t = abs(len(x) -len(y))
            x = ("0"*t)+ x
        elif (len(x) > len(y)):
            t = abs(len(x) -len(y))
            y = ("0"*t)+ y
        for i in range (min(len(x),len(y))):
            if(x[i] != y[i]):
                count += 1
        return count