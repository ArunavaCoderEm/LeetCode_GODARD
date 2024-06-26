class MyLinkedList:
    ## Easiest soln MP
    def __init__(self):
        self.list = []

    def get(self, index: int) -> int:
        if(index >= 0 and index < len(self.list) and len(self.list)):
            return self.list[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.list.insert(0,val)        

    def addAtTail(self, val: int) -> None:
        self.list.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if(index >= 0 and index <= len(self.list)):
            self.list.insert(index,val)

    def deleteAtIndex(self, index: int) -> None:
        if(index >= 0 and index < len(self.list)):
            self.list.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)