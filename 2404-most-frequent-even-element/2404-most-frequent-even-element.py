class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        x = [i for i in nums if (i % 2 == 0)]
        c = Counter(x)
        if (not x):
            return -1
        x.sort()
        for i in x:
            if(c[i] == max(c.values())):
                return i

