class MyCircularQueue:
    ## easiest question 
    def __init__(self, k: int):
        self.q = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if(self.isFull()): return False
        else:
            self.q.append(value)
            return True
    def deQueue(self) -> bool:
        if(self.isEmpty()): return False
        else:
            self.q.remove(self.q[0])
            return True
    def Front(self) -> int:
        if(self.isEmpty()): return -1
        return self.q[0]
    def Rear(self) -> int:
        if(self.isEmpty()): return -1
        return self.q[len(self.q) - 1]

    def isEmpty(self) -> bool:
        if(len(self.q) == 0): return True
        return False

    def isFull(self) -> bool:
        if(len(self.q) == self.k): return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()