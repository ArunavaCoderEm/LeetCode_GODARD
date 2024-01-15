# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,q = head,head
        res = []
        while (p != None):
            res.append(p.val)
            p = p.next
        res.sort()
        i = 0
        while (q != None):
            q.val = res[i]
            q = q.next
            i += 1
        return head