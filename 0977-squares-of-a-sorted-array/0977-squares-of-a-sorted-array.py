class Solution(object):
    def sortedSquares(self, nums):
        x = [(i**2) for i in nums]
        x.sort()
        return x
        