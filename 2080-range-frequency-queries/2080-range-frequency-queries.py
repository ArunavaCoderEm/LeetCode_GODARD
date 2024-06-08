class RangeFreqQuery:
    ## I was doing normal linear search !!
    ## same code worked with Binary search with 32 % beats !!
    ## I dont have any freaking idea how it can be optimized further !!
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.res = {}
        for i, ans in enumerate(arr):
            if (ans not in self.res):
                self.res[ans] = []
            self.res[ans].append(i)

    def ansgen(self, ansue: int, left: int, right: int) -> int:
        if (ansue not in self.res):return 0    
        idx = self.res[ansue]
        li = self.bsl(idx, left)
        ri = self.bsr(idx, right)
        
        return ri - li

    def bsl(self, idx: List[int], target: int) -> int:
        low, high = 0, len(idx)
        while low < high:
            mid = (low + high) // 2
            if idx[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def bsr(self, idx: List[int], target: int) -> int:
        low, high = 0, len(idx)
        while low < high:
            mid = (low + high) // 2
            if idx[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low

    def query(self, left: int, right: int, ansue: int) -> int:
        return self.ansgen(ansue, left, right)

# class RangeFreqQuery:

#     def __init__(self, arr: List[int]):
#         self.res = arr

#     def query(self, left: int, right: int, ansue: int) -> int:
#         c = Counter(self.res[left:right+1])
#         return c[ansue]

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,ansue)