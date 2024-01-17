# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        res = []
        p = head
        q = head
        while (p != None):
            res.append(p.val)
            p = p.next
        res[left-1:right] = res[left-1:right][::-1]
        i = 0
        while (q != None and i < len(res)):
            q.val = res[i]
            i += 1
            q = q.next
        return head