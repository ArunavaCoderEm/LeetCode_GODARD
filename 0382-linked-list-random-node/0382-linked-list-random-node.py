import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.ll = []
        if(head):
            while(head):
                self.ll.append(head.val)
                head = head.next
        else:
            self.ll.append(None)
    def getRandom(self) -> int:
        ind = random.randint(0,len(self.ll)-1)
        ele = self.ll[ind]
        return ele


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()