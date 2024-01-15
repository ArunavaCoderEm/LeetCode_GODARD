class Solution(object):
    def checkStraightLine(self, coordinates):
        x = []
        y = []
        res = []
        for i in coordinates:
            x.append(i[0])
            y.append(i[1])
        for j in range(len(y)-1):
            ybar = (y[j+1]-y[j])
            xbar = (x[j+1]-x[j])
            if(xbar == 0):
                res.append(69)
            else:
                res.append((ybar/xbar))
        return len(list(set(res))) == 1