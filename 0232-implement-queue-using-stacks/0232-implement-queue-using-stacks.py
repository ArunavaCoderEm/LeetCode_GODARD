# class MyQueue:

#     def __init__(self):
#         self.q = []

#     def push(self, x: int) -> None:
#         self.q.append(x)

#     def pop(self) -> int:
#         res = self.q.pop(0)
#         return res

#     def peek(self) -> int:
#         return self.q[0]

#     def empty(self) -> bool:
#         return True if(not len(self.q)) else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# another approach for reducing TC and it worked Basics

class MyQueue:

    def __init__(self):
        self.q = []
        self.f = 0
        self.r = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.r += 1

    def pop(self) -> int:
        res = self.q[self.f]
        self.f += 1
        return res

    def peek(self) -> int:
        return self.q[self.f]

    def empty(self) -> bool:
        return True if(self.r == self.f) else False