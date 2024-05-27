import random
class Solution:

    def __init__(self, nums: List[int]):
        self.sollist = nums
        self.d = {}
        for i in range(len(self.sollist)):
            if(self.sollist[i] not in self.d.keys()):
                self.d[self.sollist[i]] = [i]
            elif(self.sollist[i] in self.d.keys()):
                self.d[self.sollist[i]].append(i)

    def pick(self, target: int) -> int:
        n = len(self.d[target])
        x = random.randint(0,n - 1)
        return self.d[target][x] 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)