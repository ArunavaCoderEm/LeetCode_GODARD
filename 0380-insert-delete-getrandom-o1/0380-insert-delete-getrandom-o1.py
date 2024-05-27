import random
class RandomizedSet:

    def __init__(self):
        self.set = []

    def insert(self, val: int) -> bool:
        if(val not in self.set):
            self.set.append(val)
            return True
        else: return False

    def remove(self, val: int) -> bool:
        if(val in self.set):
            self.set.remove(val)
            return True
        else: return False
    def getRandom(self) -> int:
        n = len(self.set)
        x = random.randint(0,n - 1)
        if(x >= 0 and x < n):
            return self.set[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()