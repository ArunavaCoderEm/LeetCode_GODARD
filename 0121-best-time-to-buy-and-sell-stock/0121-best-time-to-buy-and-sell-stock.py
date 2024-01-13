class Solution(object):
    def maxProfit(self, prices):
        lav = 0
        minn = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minn:
                minn = prices[i]
            else:
                lav = max(lav, prices[i] - minn)
        return lav