import bisect

class MedianFinder:

    def __init__(self):
        self.ml = []
        self.l = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.ml, num)
        self.l += 1
    def findMedian(self) -> float:
        m = self.l // 2
        n = m - 1
        if(self.l % 2 == 0):
            x = (self.ml[m] + self.ml[n]) / 2
            return x
        else:
            x = self.ml[m]
            return x


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()