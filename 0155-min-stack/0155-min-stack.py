class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if(len(self.min) != 0):
            val =  min(self.min[len(self.min) - 1], val)
        self.min.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min.pop()

    def top(self) -> int:
        ele = self.stk[len(self.stk) - 1]
        return ele

    def getMin(self) -> int:
        ele = self.min[len(self.min) - 1]
        return ele


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()