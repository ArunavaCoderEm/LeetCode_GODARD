import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nsuff = nums[:]
        self.temp = nums[:]

    def reset(self) -> List[int]:
        print(self.temp)
        return self.temp

    def shuffle(self) -> List[int]:
        random.shuffle(self.nsuff)
        print(self.nsuff)
        return self.nsuff

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()