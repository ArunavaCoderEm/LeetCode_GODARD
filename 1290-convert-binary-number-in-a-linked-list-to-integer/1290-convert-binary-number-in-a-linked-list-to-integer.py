# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if (head != None):
            sum = 0
            while (head != None):
                sum = (10*sum) + head.val
                head = head.next
            return (int(str(sum),2))
        else:
            return None